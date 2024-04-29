
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns


"""
We shall be doing US only in this case 

"""

# Load the data
data = pd.read_csv("marketing_data.csv")

# Load world map data from Natural Earth Low Resolution dataset
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))

# Filter the GeoDataFrame to include only the USA
usa = world[world['iso_a3'] == 'USA']

# Create a GeoDataFrame from our marketing data
gdf = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data["Longitude"], data["Latitude"]))

# Plotting the USA map and overlaying customer locations
fig, ax = plt.subplots(figsize=(10, 6))
usa.plot(ax=ax, color='lightgrey', edgecolor='black')
gdf.plot(ax=ax, color='blue', markersize=5)
plt.title("Geospatial Distribution of Customers in the USA")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()

# Add more context and analysis
# Calculate the total number of customers
total_customers = len(data)

# Calculate the number of customers within the USA
customers_in_usa = len(gdf[gdf.within(usa.geometry.unary_union)])

# Calculate the percentage of customers within the USA
percentage_in_usa = (customers_in_usa / total_customers) * 100

print(f"Total number of customers: {total_customers}")
print(f"Number of customers within the USA: {customers_in_usa}")
print(f"Percentage of customers within the USA: {percentage_in_usa:.2f}%")
