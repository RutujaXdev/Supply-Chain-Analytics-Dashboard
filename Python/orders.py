import pandas as pd
import random
import os

# Read datasets
customers = pd.read_csv("Dataset/customers.csv")
products = pd.read_csv("Dataset/products.csv")
suppliers = pd.read_csv("Dataset/suppliers.csv")
warehouses = pd.read_csv("Dataset/warehouses.csv")
calendar = pd.read_csv("Dataset/calendar.csv")

# Lists for random selection
customer_ids = customers["customer_id"].tolist()
supplier_ids = suppliers["supplier_id"].tolist()
warehouse_ids = warehouses["warehouse_id"].tolist()
dates = calendar["date"].tolist()

payment_methods = ["UPI", "Credit Card", "Debit Card", "Cash on Delivery", "Net Banking"]
payment_weights = [45, 25, 15, 10, 5]

order_statuses = ["Delivered", "Returned", "Cancelled"]
status_weights = [90, 5, 5]

orders = []

TOTAL_ORDERS = 100000

for order_id in range(1, TOTAL_ORDERS + 1):

    # Random product
    product = products.sample(1).iloc[0]

    customer_id = random.choice(customer_ids)
    supplier_id = random.choice(supplier_ids)
    warehouse_id = random.choice(warehouse_ids)
    order_date = random.choice(dates)

    quantity = random.randint(1, 5)

    cost_price = product["cost_price"]
    selling_price = product["selling_price"]

    sales = quantity * selling_price

    discount_percent = random.choice([0, 5, 10, 15, 20])

    discount_amount = sales * discount_percent / 100

    final_sales = sales - discount_amount

    cost = quantity * cost_price

    shipping_cost = random.randint(100, 500)

    profit = final_sales - cost - shipping_cost

    payment_method = random.choices(
        payment_methods,
        weights=payment_weights,
        k=1
    )[0]

    order_status = random.choices(
        order_statuses,
        weights=status_weights,
        k=1
    )[0]

    delivery_days = random.randint(1, 10)

    orders.append({

        "order_id": f"ORD{100000 + order_id}",

        "order_date": order_date,

        "customer_id": customer_id,

        "product_id": product["product_id"],

        "supplier_id": supplier_id,

        "warehouse_id": warehouse_id,

        "quantity": quantity,

        "cost_price": cost_price,

        "selling_price": selling_price,

        "discount_percent": discount_percent,

        "discount_amount": round(discount_amount, 2),

        "sales": round(final_sales, 2),

        "cost": round(cost, 2),

        "shipping_cost": shipping_cost,

        "profit": round(profit, 2),

        "payment_method": payment_method,

        "order_status": order_status,

        "delivery_days": delivery_days

    })

# Convert to DataFrame
orders_df = pd.DataFrame(orders)

# Save CSV
os.makedirs("Dataset", exist_ok=True)

orders_df.to_csv("Dataset/orders.csv", index=False)

print("\n✅ orders.csv created successfully!")

print(orders_df.head())

print(f"\nTotal Orders: {len(orders_df)}")