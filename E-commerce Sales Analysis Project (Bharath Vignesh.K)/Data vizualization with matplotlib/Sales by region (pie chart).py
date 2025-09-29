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


# revenue column
df['Revenue'] = df['Quantity'] * df['Unit Price']

# Sales by country
sales_by_country = df.groupby('Country')['Revenue'].sum().sort_values(ascending=False)

print("Sales by country:",sales_by_country)

import matplotlib.pyplot as plt
import seaborn as sns

# Pie chart for regional sales
sales_by_country.head(5).plot(kind='pie', autopct='%1.1f%%', title='Top 5 Countries by Sales')
plt.ylabel("")
plt.show()
