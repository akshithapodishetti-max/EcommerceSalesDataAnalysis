import pandas as pd

df = pd.read_csv(
    r"C:\Users\DELL\Desktop\Ecommerce_Data_Analytics\dataset\cleaned_sales.csv"
)

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
average_order_value = total_sales / total_orders

print("===== BUSINESS KPIs =====")

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity Sold:", total_quantity)
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Average Order Value:", round(average_order_value, 2))
print("\n===== PROFIT BY CATEGORY =====")

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print(category_profit)
print("\n===== SALES BY CATEGORY =====")

category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print(category_sales)
print("\n===== SALES BY REGION =====")

region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print(region_sales)
print("\n===== PROFIT BY REGION =====")

region_profit = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)

print(region_profit)
print("\n===== TOP 10 PRODUCTS BY SALES =====")

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)
print("\n===== MONTHLY SALES =====")

monthly_sales = (
    df.groupby("Year_Month")["Sales"]
    .sum()
)

print(monthly_sales)
import matplotlib.pyplot as plt

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# Profit by Category

category_profit = (
    df.groupby("Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
category_profit.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# Sales by Region

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# Profit by Region

region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
region_profit.plot(kind="bar")

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
# Monthly Sales Trend

monthly_sales = (
    df.groupby("Year_Month")["Sales"]
    .sum()
    .sort_index()
)

plt.figure(figsize=(12, 5))
plt.plot(monthly_sales.index, monthly_sales.values)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
# Top 10 Products by Sales

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.ylabel("Product")
plt.tight_layout()
plt.show()
