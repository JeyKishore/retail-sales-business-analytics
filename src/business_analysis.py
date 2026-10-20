from pathlib import Path
import pandas as pd

# STEP 1: Define project paths

PROJECT_DIR = Path(__file__).resolve().parents[1]

DATA_FILE = (
PROJECT_DIR
/ "data"
/ "processed"
/ "superstore_clean.csv"
)

OUTPUT_DIR = PROJECT_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# STEP 2: Load cleaned data

df = pd.read_csv(
DATA_FILE,
parse_dates=["Order_Date", "Ship_Date"]
)

print("Dataset loaded:", df.shape)

# STEP 3: Calculate overall KPIs

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()
total_customers = df["Customer_ID"].nunique()
total_quantity = df["Quantity"].sum()

profit_margin = (
total_profit / total_sales * 100
if total_sales != 0
else 0
)

print("\n========== BUSINESS KPI REPORT ==========")

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Unique Customers: {total_customers:,}")
print(f"Units Sold: {total_quantity:,}")
print(f"Profit Margin: {profit_margin:.2f}%")

# STEP 4: Category performance

category_summary = (
df.groupby("Category", as_index=False)
.agg(
Sales=("Sales", "sum"),
Profit=("Profit", "sum"),
Quantity=("Quantity", "sum"),
Orders=("Order_ID", "nunique")
)
.sort_values("Sales", ascending=False)
)

category_summary.to_csv(
OUTPUT_DIR / "category_summary.csv",
index=False
)

print("\n========== CATEGORY PERFORMANCE ==========")
print(category_summary.to_string(index=False))

# STEP 5: Regional performance

region_summary = (
df.groupby("Region", as_index=False)
.agg(
Sales=("Sales", "sum"),
Profit=("Profit", "sum"),
Orders=("Order_ID", "nunique")
)
.sort_values("Sales", ascending=False)
)

region_summary.to_csv(
OUTPUT_DIR / "region_summary.csv",
index=False
)

print("\n========== REGIONAL PERFORMANCE ==========")
print(region_summary.to_string(index=False))

# STEP 6: Monthly performance

monthly_summary = (
df.groupby("Year_Month", as_index=False)
.agg(
Sales=("Sales", "sum"),
Profit=("Profit", "sum"),
Orders=("Order_ID", "nunique")
)
.sort_values("Year_Month")
)

monthly_summary.to_csv(
OUTPUT_DIR / "monthly_summary.csv",
index=False
)

print("\nMonthly summary saved.")

print("\nAnalysis completed successfully.")
print("Reports saved in:", OUTPUT_DIR)
