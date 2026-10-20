import pandas as pd
import mysql.connector
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
CSV_FILE = PROJECT_DIR / "data" / "processed" / "superstore_clean.csv"

print("Loading CSV...", flush=True)
df = pd.read_csv(CSV_FILE)

print(f"Loaded {len(df)} rows and {len(df.columns)} columns.", flush=True)

# Convert date columns to MySQL-compatible strings
for column in ["Order_Date", "Ship_Date"]:
    df[column] = pd.to_datetime(
        df[column], errors="coerce"
    ).dt.strftime("%Y-%m-%d")

# Replace missing values with None
df = df.astype(object).where(pd.notna(df), None)

print("Connecting to MySQL...", flush=True)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Enter your MySQL password: "),
    database="retail_sales_db"
)

cursor = connection.cursor()

# Create a new table with appropriate column types
column_definitions = []

for column in df.columns:
    name = f"`{column}`"

    if column in ["Order_Date", "Ship_Date"]:
        data_type = "DATE"
    elif column in ["Sales", "Profit", "Discount", "Profit_Margin"]:
        data_type = "DECIMAL(15,4)"
    elif column in [
        "Row_ID", "Quantity", "Order_Year", "Order_Month"
    ]:
        data_type = "INT"
    else:
        data_type = "VARCHAR(255)"

    column_definitions.append(f"{name} {data_type}")

print("Creating table...", flush=True)

cursor.execute("DROP TABLE IF EXISTS superstore_clean")

create_sql = f"""
CREATE TABLE superstore_clean (
    {", ".join(column_definitions)}
)
"""

cursor.execute(create_sql)
connection.commit()

column_names = ", ".join(f"`{column}`" for column in df.columns)
placeholders = ", ".join(["%s"] * len(df.columns))

insert_sql = f"""
INSERT INTO superstore_clean ({column_names})
VALUES ({placeholders})
"""

print("Importing records...", flush=True)

batch_size = 250

for start in range(0, len(df), batch_size):
    batch_df = df.iloc[start:start + batch_size]
    records = list(batch_df.itertuples(index=False, name=None))

    cursor.executemany(insert_sql, records)
    connection.commit()

    print(
        f"Imported {min(start + batch_size, len(df))} "
        f"of {len(df)} rows.",
        flush=True
    )

cursor.close()
connection.close()

print("Import completed successfully!", flush=True)