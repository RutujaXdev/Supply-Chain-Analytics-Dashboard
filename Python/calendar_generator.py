import pandas as pd
import os

# Create dates from 1 Jan 2024 to 31 Dec 2025
dates = pd.date_range(start="2024-01-01", end="2025-12-31")

calendar = pd.DataFrame({
    "date": dates,
    "day": dates.day,
    "day_name": dates.day_name(),
    "month": dates.month,
    "month_name": dates.month_name(),
    "quarter": dates.quarter,
    "year": dates.year,
    "week": dates.isocalendar().week
})

os.makedirs("Dataset", exist_ok=True)

calendar.to_csv("Dataset/calendar.csv", index=False)

print(calendar.head())
print(f"\nTotal Dates: {len(calendar)}")
print("\n✅ calendar.csv created successfully!")