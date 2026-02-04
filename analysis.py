import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("sales_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

print("\n===== SALES DATA =====")
print(df.head())

# Total Sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Best Product
best_product = df.groupby("Product")["Sales"].sum().idxmax()
print("Best Selling Product:", best_product)

# Sales by Month
df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n===== Monthly Sales =====")
print(monthly_sales)

# Plot Monthly Sales
plt.figure()
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()
