import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns
import os

'''
Utilizes an external .shp file and then does a zoom on North America 
'''


# Set the SHAPE_RESTORE_SHX config option to YES
os.environ['SHAPE_RESTORE_SHX'] = 'YES'

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

# Load world map data from Shapefile
world_path = "ne_110m_admin_0_countries_lakes.shp"
world = gpd.read_file(world_path)
# Plotting the entire world map
# Plotting the USA map and overlaying customer locations
fig, ax = plt.subplots(figsize=(10, 6))
usa.plot(ax=ax, color='lightgrey', edgecolor='black')
gdf.plot(ax=ax, color='blue', markersize=5)

# Add text annotations for longitude and latitude
# Longitude annotations
plt.text(-130, 20, "120°W", fontsize=8)
plt.text(-100, 20, "100°W", fontsize=8)
plt.text(-70, 20, "80°W", fontsize=8)
plt.text(-40, 20, "60°W", fontsize=8)
plt.text(-10, 20, "40°W", fontsize=8)
plt.text(20, 20, "20°W", fontsize=8)

# Latitude annotations
plt.text(-130, 45, "60°N", fontsize=8)
plt.text(-130, 30, "45°N", fontsize=8)
plt.text(-130, 15, "30°N", fontsize=8)
plt.text(-130, 0, "Equator", fontsize=8)
plt.text(-130, -15, "30°S", fontsize=8)
plt.text(-130, -30, "45°S", fontsize=8)
plt.text(-130, -45, "60°S", fontsize=8)

plt.title("Geospatial Distribution of Customers in the USA")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
