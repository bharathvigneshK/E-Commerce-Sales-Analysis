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

# Remove duplicates
print(df.drop_duplicates(inplace=True))

# Remove invalid rows where quantity is less than 1

# Filter invalid rows where quantity < 1
invalid_rows = df[df['Quantity'] < 1]

# Check if there are any invalid rows
if not invalid_rows.empty:
    print("Invalid rows:")
    print(invalid_rows)
else:
    print("None")


