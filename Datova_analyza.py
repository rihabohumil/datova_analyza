import pandas as pd
import matplotlib.pyplot as plt

# 1. Načtení dat
df = pd.read_csv("data/data.csv")

# 2. Vytvoření nového sloupce - celková cena objednávky
df["total_price"] = df["price"] * df["quantity"]

# 3. Celkové tržby
total_revenue = df["total_price"].sum()
print(f"Celkové tržby: {total_revenue} Kč")

# 4. Tržby podle produktu
revenue_by_product = df.groupby("product")["total_price"].sum()
print("\nTržby podle produktu:")
print(revenue_by_product)

# 5. Tržby podle regionu
revenue_by_region = df.groupby("region")["total_price"].sum()
print("\nTržby podle regionu:")
print(revenue_by_region)

# 6. Graf tržeb podle produktu
revenue_by_product.plot(kind="bar")
plt.title("Tržby podle produktu")
plt.xlabel("Produkt")
plt.ylabel("Tržby (Kč)")
plt.tight_layout()
plt.show()
