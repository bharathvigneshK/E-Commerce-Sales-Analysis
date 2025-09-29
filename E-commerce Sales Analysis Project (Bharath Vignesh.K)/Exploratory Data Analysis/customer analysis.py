import pandas as pd
import numpy as np
from random import choice, randint
from datetime import datetime, timedelta
import os
import pandas as pd

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Go up one folder (from Scripts to Data Analysis Project)
project_root = os.path.dirname(script_dir)

# Build the path to the dataset inside the Dataset folder
csv_path = os.path.join(project_root, "Dataset", "sales_data.csv")

# Load the data
df = pd.read_csv(csv_path)
print("Dataset loaded successfully!")

print(df.head(100))

# Add a revenue column
df['Revenue'] = df['Quantity'] * df['Unit Price']

print(df['Revenue'])

# Top customers
top_customers = df.groupby('Customer ID')['Revenue'].sum().sort_values(ascending=False).head(10)

print("most valuable customers:",top_customers)
