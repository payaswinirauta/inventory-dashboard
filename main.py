import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load CSV
df = pd.read_csv("inventory.csv")

# 1. Total stock by category
category_stock = df.groupby("Category")["Quantity"].sum()
print("Total stock by category:\n", category_stock)

# 2. Low stock alert (Quantity < 10)
low_stock = df[df["Quantity"] < 10]
print("\nLow stock products:\n", low_stock)

# 3. Upcoming restocks (within 7 days)
df["RestockDate"] = pd.to_datetime(df["RestockDate"])
today = datetime.today()
next_week = today + pd.Timedelta(days=7)
upcoming_restock = df[df["RestockDate"] <= next_week]
print("\nUpcoming Restocks in next 7 days:\n", upcoming_restock)

# 4. Bar chart: stock by category
category_stock.plot(kind="bar", color="skyblue")
plt.title("Total Inventory by Category")
plt.xlabel("Category")
plt.ylabel("Total Quantity")
plt.tight_layout()
plt.savefig("inventory_chart.png")  # Save image
plt.show()  # Show chart
