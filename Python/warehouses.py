import pandas as pd
import os

warehouses = [
    {"warehouse_id": 1, "warehouse_name": "Mumbai Warehouse", "city": "Mumbai", "state": "Maharashtra", "capacity": 25000},
    {"warehouse_id": 2, "warehouse_name": "Pune Warehouse", "city": "Pune", "state": "Maharashtra", "capacity": 20000},
    {"warehouse_id": 3, "warehouse_name": "Delhi Warehouse", "city": "Delhi", "state": "Delhi", "capacity": 30000},
    {"warehouse_id": 4, "warehouse_name": "Hyderabad Warehouse", "city": "Hyderabad", "state": "Telangana", "capacity": 18000},
    {"warehouse_id": 5, "warehouse_name": "Bengaluru Warehouse", "city": "Bengaluru", "state": "Karnataka", "capacity": 22000},
    {"warehouse_id": 6, "warehouse_name": "Chennai Warehouse", "city": "Chennai", "state": "Tamil Nadu", "capacity": 20000},
    {"warehouse_id": 7, "warehouse_name": "Kolkata Warehouse", "city": "Kolkata", "state": "West Bengal", "capacity": 17000},
    {"warehouse_id": 8, "warehouse_name": "Ahmedabad Warehouse", "city": "Ahmedabad", "state": "Gujarat", "capacity": 19000},
    {"warehouse_id": 9, "warehouse_name": "Jaipur Warehouse", "city": "Jaipur", "state": "Rajasthan", "capacity": 16000},
    {"warehouse_id": 10, "warehouse_name": "Lucknow Warehouse", "city": "Lucknow", "state": "Uttar Pradesh", "capacity": 15000},
    {"warehouse_id": 11, "warehouse_name": "Nagpur Warehouse", "city": "Nagpur", "state": "Maharashtra", "capacity": 18000},
    {"warehouse_id": 12, "warehouse_name": "Indore Warehouse", "city": "Indore", "state": "Madhya Pradesh", "capacity": 17000},
    {"warehouse_id": 13, "warehouse_name": "Kochi Warehouse", "city": "Kochi", "state": "Kerala", "capacity": 14000},
    {"warehouse_id": 14, "warehouse_name": "Bhubaneswar Warehouse", "city": "Bhubaneswar", "state": "Odisha", "capacity": 13000},
    {"warehouse_id": 15, "warehouse_name": "Chandigarh Warehouse", "city": "Chandigarh", "state": "Chandigarh", "capacity": 12000}
]

df = pd.DataFrame(warehouses)

os.makedirs("Dataset", exist_ok=True)

df.to_csv("Dataset/warehouses.csv", index=False)

print(df.head())
print(f"\nTotal Warehouses: {len(df)}")
print("\n✅ warehouses.csv created successfully!")