import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv("marketing_data.csv")

# Plotting temperature distribution
sns.histplot(data["Temperature (C)"], kde=True)
plt.title("Temperature Distribution")
plt.xlabel("Temperature (C)")
plt.ylabel("Frequency")
plt.show()

# Plotting purchase behavior
sns.histplot(data["Purchases"], kde=True)
plt.title("Purchase Behavior")
plt.xlabel("Number of Purchases")
plt.ylabel("Frequency")
plt.show()

# Plotting total spent distribution
sns.histplot(data["Total Spent"], kde=True)
plt.title("Total Spent Distribution")
plt.xlabel("Total Spent")
plt.ylabel("Frequency")
plt.show()

# Plotting campaign engagement
plt.figure(figsize=(8, 6))
sns.countplot(x="Campaign Engagement", data=data, order=["Low", "Medium", "High"])
plt.title("Campaign Engagement")
plt.xlabel("Engagement Level")
plt.ylabel("Count")
plt.show()

# Plotting geospatial data
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Create a GeoDataFrame from our marketing data
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data["Longitude"], data["Latitude"]))

# Plotting the cities on the map
fig, ax = plt.subplots(figsize=(10, 6))
world.plot(ax=ax, color='lightgrey', edgecolor='black')
gdf.plot(ax=ax, color='blue', markersize=5)
plt.title("Geospatial Distribution of Customers")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
