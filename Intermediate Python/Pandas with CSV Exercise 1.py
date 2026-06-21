"""
Human Resources sent you an employee file named employee_records.csv. Some employees didn't get a bonus this year, so their "Bonus" column is completely blank (missing data). You need to fix these blank spaces and then find all the employees who work in a specific department.
(Assume the CSV has columns: Name, Department, Salary, and Bonus).

Tasks:
1. Import Pandas and load "employee_records.csv" into a DataFrame named df.
2. The "Bonus" column has missing data (NaN). Use a Pandas method to fill all those missing values with 0. Save this fixed data back to the df or print it directly.
3. HR only wants to see the Engineering team right now. Create a new variable called engineering_team that filters the DataFrame to only show rows where the "Department" is exactly equal to "Engineering".
4.Print the engineering_team DataFrame.

NOTE: This is only an example CSV file for better understanding
"""

import pandas as pd

# 1. Loading the hypothetical CSV file
df = pd.read_csv("employee_records.csv")

# 2. Filling missing bonus data with 0
# The inplace=True argument permanently updates the existing DataFrame, 
# or you could do: df["Bonus"] = df["Bonus"].fillna(0)
df["Bonus"].fillna(0, inplace=True) 

# 3. Filtering the DataFrame
engineering_team = df[df["Department"] == "Engineering"]

# 4. Printing the final filtered result
print("--- Engineering Department Data ---")
print(engineering_team)
