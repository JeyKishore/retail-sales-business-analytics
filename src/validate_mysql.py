import pandas as pd
import mysql.connector

# Load the historical CSV
csv_path = "data/processed/superstore_historical.csv"
df_csv = pd.read_csv(csv_path)

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=input("Enter your MySQL root password: "),
    database="retail_sales_db"
)

# Load data from MySQL
query = """
SELECT
    Row_ID,
    Sales,
    Profit,
    Profit_Margin
FROM superstore_historical
ORDER BY Row_ID
"""

df_sql = pd.read_sql(query, conn)
conn.close()

# Sort CSV data by Row_ID
df_csv = df_csv.sort_values("Row_ID").reset_index(drop=True)
df_sql = df_sql.sort_values("Row_ID").reset_index(drop=True)

# Compare row counts
print("\n--- ROW COUNT VALIDATION ---")
print("CSV rows:", len(df_csv))
print("MySQL rows:", len(df_sql))

# Compare row IDs
print("\n--- ROW ID VALIDATION ---")
print(
    "All Row_ID values match:",
    df_csv["Row_ID"].equals(df_sql["Row_ID"])
)

# Compare numeric columns
print("\n--- NUMERIC VALIDATION ---")

for column in ["Sales", "Profit", "Profit_Margin"]:
    csv_values = pd.to_numeric(df_csv[column], errors="coerce")
    sql_values = pd.to_numeric(df_sql[column], errors="coerce")

    differences = (csv_values - sql_values).abs()
    mismatches = differences > 0.000001

    print(f"\n{column}:")
    print("Mismatched rows:", int(mismatches.sum()))

    if mismatches.any():
        print("Sample mismatches:")
        print(
            pd.DataFrame({
                "Row_ID": df_csv.loc[mismatches, "Row_ID"],
                "CSV_Value": csv_values[mismatches],
                "MySQL_Value": sql_values[mismatches],
                "Difference": differences[mismatches]
            }).head(10).to_string(index=False)
        )

print("\nValidation completed.")