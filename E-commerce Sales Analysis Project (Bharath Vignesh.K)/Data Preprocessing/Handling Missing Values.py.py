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
df= pd.read_csv(csv_path)
print("Dataset loaded successfully!")


print(df)

# Assuming you already have the dataframe loaded as 'df'
# Display the entire dataframe (if it's not too large)
pd.set_option('display.max_rows', None)  # This will allow you to display all rows
pd.set_option('display.max_columns', None)  # This will allow you to display all columns

'''print(df.head(100))'''
# Handling missing values
print(df.dropna(inplace=True))  # or use df.fillna(method='ffill'), etc.



