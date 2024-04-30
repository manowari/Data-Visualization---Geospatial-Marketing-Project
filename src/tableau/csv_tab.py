import pandas as pd
from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_projects_dataframe



'''
Mysql is the data source

Remmeber to change the values to your server params 

'''





# Define Tableau Server connection parameters
server_url = 'https://your-tableau-server.com'
username = 'your_username'
password = 'your_password'
site_id = 'your_site_id'

# Read data from CSV into a DataFrame
csv_file_path = 'marketing_data.csv'
data = pd.read_csv(csv_file_path)

# Connect to Tableau Server
conn = TableauServerConnection(server_url, username, password, site_id=site_id)

# Publish DataFrame to Tableau Server
project_name = 'Project Name'
overwrite = True  # Set to True if you want to overwrite an existing workbook with the same name

conn.sign_in()
project_id = get_projects_dataframe(conn).id[project_name]

temp_csv_path = 'temp_data.csv'  # Temporary CSV file path
data.to_csv(temp_csv_path, index=False)  # Write DataFrame to CSV

conn.publish_workbook(temp_csv_path, project_id, overwrite)  # Publish CSV to Tableau Server

conn.sign_out()
