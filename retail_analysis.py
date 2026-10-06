import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])

print("===== RETAIL SALES ANALYSIS =====")
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Orders:", df["Order_ID"].nunique())
print("Average Order Value:", round(df["Sales"].mean(), 2))
print("\nSales by Category:")
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))
print("\nSales by Region:")
print(df.groupby("Region")["Sales"].sum().sort_values(ascending=False))

# Category chart
df.groupby("Category")["Sales"].sum().sort_values(ascending=False).plot(kind="bar")
plt.title("Sales by Product Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()
