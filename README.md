# 📊 Retail Sales & Business Analytics Dashboard

An end-to-end data analytics project using Python, MySQL, SQL, and Power BI to analyze retail sales, profitability, regional performance, and monthly sales trends.

## 🎯 Project Overview

This project demonstrates an end-to-end data analytics workflow, from data cleaning and preparation to SQL-based analysis and interactive dashboard development.

The goal is to transform raw retail data into meaningful business insights that support data-driven decision-making.

## 🛠️ Technologies Used

- **Python** — Data cleaning, analysis, and chart generation
- **Pandas & NumPy** — Data manipulation and numerical analysis
- **MySQL** — Database storage and SQL analysis
- **SQL** — Business queries and data validation
- **Power BI** — Interactive dashboards and KPI reporting
- **Git & GitHub** — Version control and project sharing

## 📈 Key Performance Indicators

The historical dataset contains 9,145 records.

| Metric | Value |
|---|---:|
| Total Sales | $2,092,235.73 |
| Total Profit | $268,126.83 |
| Total Orders | 4,565 |
| Profit Margin | 12.82% |
| Average Order Value | $458.32 |
| Records Analyzed | 9,145 |

## 📊 Dashboard Features

The interactive Power BI dashboard includes:

- **Total Sales:** Overall sales revenue
- **Total Profit:** Overall profit generated
- **Total Orders:** Number of distinct orders
- **Profit Margin:** Profit as a percentage of sales
- **Sales by Category:** Comparison of Technology, Furniture, and Office Supplies
- **Profit by Region:** Comparison of regional profitability
- **Monthly Sales Trend:** Analysis of sales over time
- **Interactive Slicers:** Filter results by Region, Category, and Segment

## 🔄 Project Workflow

1. **Data Cleaning:** Cleaned and prepared retail data using Python and Pandas.
2. **Historical Data Preparation:** Created a historical dataset containing orders dated on or before October 20, 2026.
3. **Business Analysis:** Analyzed sales, profit, categories, and regions using Python.
4. **Data Visualization:** Generated charts and summary reports.
5. **Database Integration:** Loaded the historical dataset into MySQL.
6. **Data Validation:** Compared all 9,145 rows between the CSV and MySQL for Row_ID, Sales, Profit, and Profit_Margin.
7. **Dashboard Development:** Built an interactive Power BI dashboard using the MySQL historical table.

## 🗄️ MySQL Database

**Database:** `retail_sales_db`

**Table:** `superstore_historical`

Example SQL query:

```sql
SELECT
    COUNT(*) AS total_rows,
    ROUND(SUM(Sales), 2) AS total_sales,
    ROUND(SUM(Profit), 2) AS total_profit,
    ROUND(
        SUM(Profit) / NULLIF(SUM(Sales), 0) * 100,
        2
    ) AS profit_margin_percent,
    COUNT(DISTINCT Order_ID) AS total_orders,
    ROUND(
        SUM(Sales) / NULLIF(COUNT(DISTINCT Order_ID), 0),
        2
    ) AS average_order_value
FROM retail_sales_db.superstore_historical;


📁 Project Structure

retail-sales-business-analytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   ├── category_summary.csv
│   ├── region_summary.csv
│   ├── monthly_summary.csv
│   ├── sales_by_category.png
│   ├── profit_by_region.png
│   └── monthly_sales_trend.png
│
├── sql/
│
├── src/
│   ├── analyze_retail.py
│   ├── business_analysis.py
│   ├── clean_retail.py
│   ├── create_charts.py
│   ├── import_to_mysql.py
│   └── validate_mysql.py
│
├── Retail_Sales_Business_Analytics.pbix
└── README.md


💡 Business Questions Explored

Which product categories generate the most sales?
Which regions generate the most profit?
How do sales change over time?
What are the overall sales, profit, and profit margin?
What is the average order value?
🔍 Data Validation

The historical CSV and MySQL table were compared across all 9,145 rows for the following fields:

Row_ID
Sales
Profit
Profit_Margin

Result: No mismatches were found in these comparisons.

⚠️ Data Notes

The historical dataset includes orders dated on or before October 20, 2026.
The original cleaned dataset was retained separately.
The historical date cutoff is a project decision, not a claim that later-dated source records are invalid.
The results reflect the available dataset and are not live business data.


🚀 Future Improvements

Automate data refresh and ingestion.
Expand product-level and customer-level analysis.
Add additional business KPIs.
Improve dashboard deployment and documentation.



👨‍💻 Author

Jey Kishore K

LinkedIn: https://www.linkedin.com/in/jey-kishore-k