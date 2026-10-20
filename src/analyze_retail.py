from pathlib import Path
import pandas as pd

# STEP 1: Locate the project folder

PROJECT_DIR = Path(__file__).resolve().parents[1]

# STEP 2: Locate the raw dataset folder

DATA_DIR = PROJECT_DIR / "data" / "raw"

# STEP 3: Find supported dataset files

supported_extensions = ["*.csv", "*.xls", "*.xlsx"]
data_files = []

for extension in supported_extensions:
    data_files.extend(DATA_DIR.glob(extension))

# STEP 4: Check whether a dataset exists

if not data_files:
    raise FileNotFoundError(
"No CSV or Excel file found inside data/raw."
)

# STEP 5: Select the dataset

file_path = data_files[0]

# STEP 6: Load the dataset

if file_path.suffix.lower() == ".csv":
    df = pd.read_csv(file_path, encoding="utf-8-sig")
else:
    df = pd.read_excel(file_path)

# STEP 7: Display dataset information

print("\n========== RETAIL SALES ANALYSIS ==========")

print("\nDataset loaded successfully:", file_path.name)

print("\nFirst five rows:")
print(df.head().to_string())

print("\nDataset dimensions:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types and non-null values:")
df.info()

print("\nMissing values by column:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())
