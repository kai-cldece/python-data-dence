"""
One of the most useful and famous framework or library for data science programming is the Pandas.
The core of Pandas is its DataFrame. Pandas' DataFrame can be interpretedas an invisible spreadsheet.
It is a high powered library that interprets the data in rows and columns allowing you to filter out 
and analyze the data presented.
"""

#We are going to import the pandas library as "pd" for short term to save typing and look more organized.
#Importing pandas in this way is also applicable to other libraries especially if the program is large.

import pandas as pd
# Our basic raw data (a dictionary of lists)
shop_data = {
    "Day": ["Monday", "Tuesday", "Wednesday"],
    "Customers": [45, 52, 61],
    "Revenue": [180.50, 210.00, 250.75]
}

# Converting it into a Pandas DataFrame
df = pd.DataFrame(shop_data)
print(df)
