import pandas as pd
from tableau_api_lib import TableauServerConnection
from tableau_api_lib.utils.querying import get_projects_dataframe
from sqlalchemy import create_engine


'''
Mysql is the data source

Remmeber to change the values to your server params 

'''


# Define MySQL connection parameters
mysql_host = 'your param'
mysql_user = 'your param'
mysql_password = 'your param'
mysql_database = 'your param'

# Define Tableau Server connection parameters
server_url = 'https://your param-tableau-server.com'
username = 'your param'
password = 'your param'
site_id = 'your param'

# Connect to MySQL database
mysql_engine = create_engine(f'mysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_database}')

# Read data from MySQL into a DataFrame
query = 'SELECT * FROM your param'
data = pd.read_sql(query, mysql_engine)

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
