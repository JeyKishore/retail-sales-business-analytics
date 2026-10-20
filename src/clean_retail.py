from pathlib import Path
import pandas as pd

# STEP 1: Define project folders

PROJECT_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# STEP 2: Load the original dataset

file_path = RAW_DIR / "sample_-_superstore.xls"

df = pd.read_excel(file_path)

print("Original dataset shape:", df.shape)

# STEP 3: Standardize column names

df.columns = [
    str(column).strip()
    .replace("*", "_")
    .replace("/", "_")
    .replace(" ", "_")
    for column in df.columns
]

print("\nStandardized columns:")
print(df.columns.tolist())

# STEP 4: Convert dates

df["Order_Date"] = pd.to_datetime(
df["Order_Date"], errors="coerce"
)

df["Ship_Date"] = pd.to_datetime(
df["Ship_Date"], errors="coerce"
)

# STEP 5: Convert numeric columns

numeric_columns = ["Sales", "Profit", "Quantity", "Discount"]

for column in numeric_columns:
    df[column] = pd.to_numeric(
df[column], errors="coerce"
)

# STEP 6: Remove exact duplicate rows

initial_rows = len(df)

df = df.drop_duplicates().copy()

duplicates_removed = initial_rows - len(df)

# STEP 7: Remove rows missing essential analysis fields

rows_before_validation = len(df)

required_columns = [
"Order_ID",
"Order_Date",
"Sales",
"Profit",
"Quantity"
]

df = df.dropna(subset=required_columns).copy()

invalid_rows_removed = rows_before_validation - len(df)

# STEP 8: Create analytical columns

df["Order_Year"] = df["Order_Date"].dt.year

df["Order_Month"] = df["Order_Date"].dt.month

df["Year_Month"] = (
df["Order_Date"].dt.to_period("M").astype(str)
)

df["Profit_Margin"] = (
df["Profit"] / df["Sales"].where(df["Sales"] != 0)
)

# STEP 9: Export the cleaned dataset

output_file = PROCESSED_DIR / "superstore_clean.csv"

df.to_csv(output_file, index=False)

# STEP 10: Print the cleaning report

print("\n========== DATA CLEANING REPORT ==========")

print("Original rows:", initial_rows)
print("Exact duplicates removed:", duplicates_removed)
print("Invalid rows removed:", invalid_rows_removed)
print("Final rows:", len(df))
print("Final columns:", len(df.columns))

print("\nMissing values after cleaning:")
print(df.isnull().sum().to_string())

print("\nCleaned dataset saved successfully:")
print(output_file)
