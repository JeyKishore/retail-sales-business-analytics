from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Locate project folders

PROJECT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = PROJECT_DIR / "outputs"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load summary reports

category = pd.read_csv(OUTPUT_DIR / "category_summary.csv")
region = pd.read_csv(OUTPUT_DIR / "region_summary.csv")
monthly = pd.read_csv(OUTPUT_DIR / "monthly_summary.csv")

# Chart 1: Sales by category

category = category.sort_values("Sales", ascending=False)

plt.figure(figsize=(9, 5))
plt.bar(category["Category"], category["Sales"])
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales ($)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "sales_by_category.png", dpi=150)
plt.close()

# Chart 2: Profit by region

region = region.sort_values("Profit", ascending=False)

plt.figure(figsize=(9, 5))
plt.bar(region["Region"], region["Profit"])
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit ($)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "profit_by_region.png", dpi=150)
plt.close()

# Chart 3: Monthly sales trend

monthly["Year_Month"] = pd.to_datetime(
monthly["Year_Month"], errors="coerce"
)
monthly = monthly.sort_values("Year_Month")

plt.figure(figsize=(12, 5))
plt.plot(
monthly["Year_Month"],
monthly["Sales"],
marker="o"
)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_sales_trend.png", dpi=150)
plt.close()

print("Charts generated successfully:")
print(OUTPUT_DIR / "sales_by_category.png")
print(OUTPUT_DIR / "profit_by_region.png")
print(OUTPUT_DIR / "monthly_sales_trend.png")
