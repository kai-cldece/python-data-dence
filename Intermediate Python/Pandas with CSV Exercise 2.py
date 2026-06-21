"""
You work for a retail company and just downloaded yesterday's sales data into a file called sales_data.csv. You need to load it into Python, check the structure to make sure it loaded correctly, and calculate the total money made.
(Assume the CSV has columns: Transaction_ID, Item, Quantity, and Revenue).

TASKS:
Import the Pandas library.
Load the file "sales_data.csv" into a DataFrame named df.
Print the first 5 rows of the DataFrame to visually check the data.
Print the summary information (data types and non-null counts) of the DataFrame.
Calculate the total sum of the "Revenue" column and print it.
"""

import pandas as pd

# 1 & 2. Loading the hypothetical CSV file
df = pd.read_csv("sales_data.csv")

# 3. Checking the first 5 rows
print("--- First 5 Rows ---")
print(df.head())

# 4. Checking the structure and data types
print("\n--- DataFrame Info ---")
df.info()

# 5. Calculating total revenue
total_revenue = df["Revenue"].sum()
print(f"\nTotal Revenue for the day: ${total_revenue}")
