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


# Convert invoice date to datetime
df['Invoice Date'] = pd.to_datetime(df['Invoice Date'],dayfirst=True)
print(df['Invoice Date'])

# Extract time-based features
df['Year'] = df['Invoice Date'].dt.year
df['Month'] = df['Invoice Date'].dt.month
df['Day'] = df['Invoice Date'].dt.day
df['Hour'] = df['Invoice Date'].dt.hour
df['Weekday'] = df['Invoice Date'].dt.day_name()

# Add a revenue column
df['Revenue'] = df['Quantity'] * df['Unit Price']

# Sales over time
sales_by_month = df.groupby('Month')['Revenue'].sum()
sales_by_hour = df.groupby('Hour')['Revenue'].sum()
sales_by_day = df.groupby('Day')['Revenue'].sum()

import matplotlib.pyplot as plt
import seaborn as sns

# Monthly sales trend (Line chart)
sales_by_month.plot(kind='line', y='Total Sales', figsize=(10,6),marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()
