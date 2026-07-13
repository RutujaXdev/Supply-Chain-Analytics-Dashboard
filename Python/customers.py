import pandas as pd
from faker import Faker
import random
import os

# Create Faker object
fake = Faker("en_IN")

# Cities
cities = [
    "Mumbai",
    "Pune",
    "Delhi",
    "Hyderabad",
    "Bengaluru",
    "Chennai",
    "Kolkata",
    "Ahmedabad",
    "Jaipur",
    "Lucknow"
]

# City -> State
states = {
    "Mumbai": "Maharashtra",
    "Pune": "Maharashtra",
    "Delhi": "Delhi",
    "Hyderabad": "Telangana",
    "Bengaluru": "Karnataka",
    "Chennai": "Tamil Nadu",
    "Kolkata": "West Bengal",
    "Ahmedabad": "Gujarat",
    "Jaipur": "Rajasthan",
    "Lucknow": "Uttar Pradesh"
}

customers = []

# Generate 1000 customers
for customer_id in range(1001, 2001):

    city = random.choice(cities)

    customers.append({
        "customer_id": customer_id,
        "customer_name": fake.name(),
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(18, 65),
        "city": city,
        "state": states[city]
    })

# Convert list to DataFrame
df = pd.DataFrame(customers)

# Create Dataset folder if it doesn't exist
os.makedirs("Dataset", exist_ok=True)

# Save CSV
df.to_csv("Dataset/customers.csv", index=False)

print("✅ customers.csv created successfully!")
print(df.head())