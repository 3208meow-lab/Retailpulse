
from pathlib import Path

charts_dir = Path("charts")
charts_dir.mkdir(exist_ok=True)

import pandas as pd

df = pd.read_csv("samplesuperstore.csv")

print(df.shape)
print(df.columns)
df.info()
 # print(df.duplicated().sum())

 #  duplicates = df[df.duplicated()]
# print(duplicates)

#df = df.drop_duplicates()
#print(df.shape)

duplicates = df[df.duplicated()]
print(duplicates)

df = df.drop_duplicates()
print(df.shape)

df.isnull().sum()
print(df.isnull().sum())

print(df.describe())

print(df[df["Quantity"] <= 0])
print(df[(df["Discount"] < 0) | (df["Discount"] > 1)])
print(df[df["Sales"] <= 0])
print((df["Profit"] < 0).sum())

print(df["Category"].unique())
print(df["Region"].unique())
print(df["Segment"].unique())
print(df["Ship Mode"].unique())


print(df.shape)
print(df.duplicated().sum())
print(df.isnull().sum().sum())




# Checkpoint 7.1 — Basic Sales and Profit Analysis

print("Total Sales:", round(df["Sales"].sum(), 2))
print("Average Sales per Row:", round(df["Sales"].mean(), 2))

print("Total Profit:", round(df["Profit"].sum(), 2))
print("Average Profit per Row:", round(df["Profit"].mean(), 2))



# Checkpoint 7.2 — Category-wise Sales and Profit

category_summary = df.groupby("Category")[["Sales", "Profit"]].sum()

print(category_summary.sort_values(by="Sales", ascending=False))


# Checkpoint 7.3 — Subcategory-wise Analysis

subcategory_summary = df.groupby("Sub-Category")[["Sales", "Profit"]].sum()

print(subcategory_summary.sort_values(by="Profit", ascending=False))


# Checkpoint 7.4 — Region-wise Analysis

region_summary = df.groupby("Region")[["Sales", "Profit"]].sum()

print(region_summary.sort_values(by="Sales", ascending=False))




# Checkpoint 7.5 — Customer Segment Analysis

segment_summary = df.groupby("Segment")[["Sales", "Profit"]].sum()

print(segment_summary.sort_values(by="Sales", ascending=False))


# Checkpoint 7.6 — Ship Mode Analysis

ship_summary = df.groupby("Ship Mode")[["Sales", "Profit"]].sum()

print(ship_summary.sort_values(by="Sales", ascending=False))


# Checkpoint 7.7 — State-wise Analysis

state_summary = df.groupby("State")[["Sales", "Profit"]].sum()

print(state_summary.sort_values(by="Profit", ascending=False))



# Checkpoint 7.8 — Discount-wise Analysis

discount_summary = df.groupby("Discount")[["Sales", "Profit"]].sum()

print(discount_summary.sort_index())


# Checkpoint 7.9 — Quantity-wise Analysis

quantity_summary = df.groupby("Quantity")[["Sales", "Profit"]].sum()

print(quantity_summary.sort_index())



# Checkpoint 7.10 — City-wise Analysis

city_summary = df.groupby("City")[["Sales", "Profit"]].sum()

print(city_summary.sort_values(by="Profit", ascending=False).head(10))


# Checkpoint 7.11 — Loss-making Cities

city_summary = df.groupby("City")[["Sales", "Profit"]].sum()

loss_making_cities = city_summary[city_summary["Profit"] < 0]

print(loss_making_cities.sort_values(by="Profit").head(10))


# Checkpoint 7.12 — Category Analysis for Philadelphia

philly_data = df[df["City"] == "Philadelphia"]

philly_category_summary = philly_data.groupby("Category")[["Sales", "Profit"]].sum()

print(philly_category_summary.sort_values(by="Profit"))


# Checkpoint 7.13 — Furniture Subcategory Analysis

philly_furniture = philly_data[
    philly_data["Category"] == "Furniture"
]

furniture_subcategory_summary = philly_furniture.groupby(
    "Sub-Category"
)[["Sales", "Profit"]].sum()

print(furniture_subcategory_summary.sort_values(by="Profit"))

# Checkpoint 8.1 — Profit Margin Analysis

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()

profit_margin = (total_profit / total_sales) * 100

print("Overall Profit Margin:", round(profit_margin, 2), "%")

# Checkpoint 8.2 — Correlation Analysis

correlation = df[["Sales", "Quantity", "Discount", "Profit"]].corr()

print(correlation.round(2))

# Checkpoint 8.3 — Statistical Summary

print(df[["Sales", "Quantity", "Discount", "Profit"]].describe().round(2))

# Checkpoint 8.4 — Outlier Review

for column in ["Sales", "Profit"]:
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)

    iqr = q3 - q1

    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print(column, "potential outliers:", len(outliers))

# checkpoint 9.1

import matplotlib.pyplot as plt


# Checkpoint 9.1 — Sales and Profit by Category

category_summary = df.groupby("Category")[["Sales", "Profit"]].sum()

category_summary.plot(kind="bar", figsize=(9, 5))

plt.title("Sales and Profit by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Amount")
plt.xticks(rotation=0)
plt.legend(["Sales", "Profit"])
plt.tight_layout()

plt.savefig(charts_dir / "category_sales_profit.png",
            dpi=300, bbox_inches="tight")
plt.show()




# Checkpoint 9.2 — Profit by Sub-Category

subcategory_profit = df.groupby("Sub-Category")["Profit"].sum()
subcategory_profit = subcategory_profit.sort_values()

subcategory_profit.plot(kind="bar", figsize=(11, 6))

plt.title("Profit by Product Sub-Category")
plt.xlabel("Product Sub-Category")
plt.ylabel("Total Profit")
plt.axhline(y=0, color="black", linewidth=0.8)
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(charts_dir / "subcategory_profit.png",
            dpi=300, bbox_inches="tight")
plt.show()




# Checkpoint 9.3 — Sales and Profit by Region

region_summary = df.groupby("Region")[["Sales", "Profit"]].sum()

region_summary.plot(kind="bar", figsize=(8, 5))

plt.title("Sales and Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Amount")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(charts_dir / "region_sales_profit.png",
            dpi=300, bbox_inches="tight")
plt.show()




# Checkpoint 9.4 — Average Profit by Discount Level

discount_profit = df.groupby("Discount")["Profit"].mean()

discount_profit.plot(kind="bar", figsize=(9, 5))

plt.title("Average Profit by Discount Level")
plt.xlabel("Discount")
plt.ylabel("Average Profit per Row")
plt.axhline(y=0, color="black", linewidth=0.8)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(charts_dir / "discount_profit.png",
            dpi=300, bbox_inches="tight")
plt.show()
