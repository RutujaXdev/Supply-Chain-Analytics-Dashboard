import pandas as pd
import random
import os

# Product Catalog
products_data = {
    "Electronics": {
        "Dell": [
            "Inspiron 15",
            "XPS 13",
            "Latitude 5420"
        ],
        "HP": [
            "Pavilion 14",
            "Victus 15",
            "Envy x360"
        ],
        "Lenovo": [
            "ThinkPad E14",
            "IdeaPad Slim 5",
            "Legion 5"
        ],
        "Apple": [
            "MacBook Air M3",
            "MacBook Pro 14",
            "iPad Air"
        ],
        "Asus": [
            "ROG Strix G16",
            "Vivobook 15",
            "Zenbook 14"
        ]
    },

    "Home Appliances": {
        "LG": [
            "260L Refrigerator",
            "1.5 Ton AC",
            "Front Load Washing Machine"
        ],
        "Samsung": [
            "Double Door Refrigerator",
            "55 Inch Smart TV",
            "Microwave Oven"
        ],
        "Whirlpool": [
            "Top Load Washing Machine",
            "Single Door Refrigerator"
        ]
    },

    "Furniture": {
        "Godrej": [
            "Office Desk",
            "Wooden Cupboard"
        ],
        "IKEA": [
            "Study Table",
            "Bookshelf"
        ],
        "Nilkamal": [
            "Office Chair",
            "Plastic Storage Cabinet"
        ]
    },

    "Accessories": {
        "Logitech": [
            "Wireless Mouse",
            "Mechanical Keyboard"
        ],
        "Boat": [
            "Bluetooth Speaker",
            "Neckband"
        ],
        "Sony": [
            "WH-1000XM5 Headphones",
            "Portable Speaker"
        ],
        "JBL": [
            "Flip 6 Speaker",
            "Tune 770NC Headphones"
        ]
    }
}

products = []

product_id = 101

for category, brands in products_data.items():

    for brand, items in brands.items():

        for item in items:

            cost_price = random.randint(5000, 80000)

            selling_price = int(cost_price * random.uniform(1.15, 1.35))

            products.append({
                "product_id": product_id,
                "product_name": item,
                "category": category,
                "brand": brand,
                "cost_price": cost_price,
                "selling_price": selling_price
            })

            product_id += 1

# Convert to DataFrame
df = pd.DataFrame(products)

# Create Dataset folder if it doesn't exist
os.makedirs("Dataset", exist_ok=True)

# Save CSV
df.to_csv("Dataset/products.csv", index=False)

print("✅ products.csv created successfully!\n")

print(df.head())

print(f"\nTotal Products: {len(df)}")