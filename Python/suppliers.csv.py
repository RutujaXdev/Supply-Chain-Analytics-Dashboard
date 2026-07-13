import pandas as pd
import random
import os

supplier_names = [
    "Tech Distributors Pvt Ltd",
    "Smart Electronics India",
    "Future Retail Supply",
    "Vision Supply Co.",
    "Elite Components",
    "National Traders",
    "Prime Wholesale",
    "Digital World Suppliers",
    "Modern Electronics",
    "Global Supply Hub",
    "Shree Enterprises",
    "Apex Distribution",
    "Infinity Traders",
    "Reliable Suppliers",
    "SuperTech Wholesale",
    "Bright India Supply",
    "Vertex Distributors",
    "NextGen Supplies",
    "Metro Traders",
    "Universal Electronics"
]

countries = [
    "India",
    "China",
    "Japan",
    "South Korea",
    "Vietnam"
]

suppliers = []

supplier_id = 1

for supplier in supplier_names:

    suppliers.append({
        "supplier_id": supplier_id,
        "supplier_name": supplier,
        "country": random.choice(countries),
        "lead_time_days": random.randint(2, 15),
        "rating": round(random.uniform(3.5, 5.0), 1)
    })

    supplier_id += 1

df = pd.DataFrame(suppliers)

os.makedirs("Dataset", exist_ok=True)

df.to_csv("Dataset/suppliers.csv", index=False)

print(df.head())
print(f"\nTotal Suppliers: {len(df)}")
print("\n✅ suppliers.csv created successfully!")