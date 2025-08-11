import pandas as pd
import matplotlib.pyplot as plt

#Create sample CSV
data = {
    "Date": pd.date_range(start="2024-01-01", periods=12, freq="M").repeat(3),
    "Product": ["Laptop", "Mobile", "Tablet"] * 12,
    "Region": ["North", "South", "East"] * 12,
    "Sales": [20000, 15000, 12000, 22000, 16000, 13000, 25000, 17000, 14000, 24000, 18000, 15000] * 3
}
df_sample = pd.DataFrame(data)
df_sample.to_csv("sales_data.csv", index=False)

#Load CSV file
df = pd.read_csv("sales_data.csv")

#Basic data overview
print("First 5 rows of the data:")
print(df.head())
print("\nDataset Info:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())

#Group by product and calculate total sales
product_sales = df.groupby("Product")["Sales"].sum().reset_index()
print("\nTotal sales by product:")
print(product_sales)

#Plot sales by product
plt.figure(figsize=(8,5))
plt.bar(product_sales["Product"], product_sales["Sales"], color="skyblue")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.title("Total Sales by Product")
plt.xticks(rotation=45)
plt.show()

#Group by region and calculate total sales
region_sales = df.groupby("Region")["Sales"].sum().reset_index()
print("\nTotal sales by region:")
print(region_sales)

#Plot sales by region
plt.figure(figsize=(8,5))
plt.bar(region_sales["Region"], region_sales["Sales"], color="orange")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.title("Total Sales by Region")
plt.xticks(rotation=45)
plt.show()

#Monthly sales trend
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()
plt.figure(figsize=(10,5))
plt.plot(monthly_sales["Month"].astype(str), monthly_sales["Sales"], marker='o')
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.show()
