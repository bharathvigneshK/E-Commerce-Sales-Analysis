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


# Add a revenue column
df['Revenue'] = df['Quantity'] * df['Unit Price']

print(df['Revenue'])

# Top-selling products by quantity and revenue
top_products = df.groupby('Description').agg({
    'Quantity': 'sum',
    'Revenue': 'sum'
}).sort_values(by='Quantity', ascending=False).head(10)

print("Top-selling-products:",top_products)

import matplotlib.pyplot as plt
import seaborn as sns

# Top 10 product sales (Bar chart)
top_products['Quantity'].plot(kind='bar', figsize=(10,6))
plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.ylim(50000,60000)
plt.xticks(rotation=45)
plt.show()
