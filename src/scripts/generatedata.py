import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from random import uniform, choice, randint

# Generate sample data
num_records = 1000

# Generate timestamps
start_date = datetime(2024, 1, 1)
timestamps = [start_date + timedelta(hours=i) for i in range(num_records)]

# Generate latitude and longitude for cities
cities = {
    "New York": (40.7128, -74.0060),
    "Los Angeles": (34.0522, -118.2437),
    "Chicago": (41.8781, -87.6298),
    "Houston": (29.7604, -95.3698),
    "Phoenix": (33.4484, -112.0740)
}

# Generate temperature readings
temperatures = [round(uniform(0, 30), 2) for _ in range(num_records)]

# Assign cities randomly to each record
city_choices = list(cities.keys())
city_column = [choice(city_choices) for _ in range(num_records)]

# Generate customer demographics
genders = ["Male", "Female"]
ages = [randint(18, 70) for _ in range(num_records)]
incomes = [round(uniform(20000, 100000), 2) for _ in range(num_records)]

# Generate purchase behavior
purchases = [randint(0, 10) for _ in range(num_records)]
total_spent = [round(purchases[i] * uniform(10, 100), 2) for i in range(num_records)]

# Generate marketing campaign engagement
campaign_engagement = [choice(["High", "Medium", "Low"]) for _ in range(num_records)]

# Create DataFrame
data = pd.DataFrame({
    "Timestamp": timestamps,
    "Latitude": [cities[city][0] for city in city_column],
    "Longitude": [cities[city][1] for city in city_column],
    "Temperature (C)": temperatures,
    "City": city_column,
    "Gender": [choice(genders) for _ in range(num_records)],
    "Age": ages,
    "Income": incomes,
    "Purchases": purchases,
    "Total Spent": total_spent,
    "Campaign Engagement": campaign_engagement
})

# Save data to CSV
data.to_csv("marketing_data.csv", index=False)
