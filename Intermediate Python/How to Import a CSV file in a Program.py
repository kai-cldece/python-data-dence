# 1. Data programming using the raw tools of Python

#Note: The CSV file included in this explanation is just an example, there's no such as students.csv. You can search up and download actual datasets in CSV file format at kaggle.com 

import csv

# 1. Open the CSV file in 'read' mode ('r')
with open('students.csv', 'r') as file:
    
    # 2. Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # 3. Extract the header row (Name, Subject, Grade)
    header = next(csv_reader)
    print(f"The columns are: {header}")
    print("-" * 30)
    
    # 4. Loop through the remaining rows in the file
    for row in csv_reader:
        # Each 'row' is a list of strings
        name = row[0]
        subject = row[1]
        grade = row[2]
        
        print(f"Student {name} scored {grade} in {subject}.")


# 2. Using the Pandas library to interpret the CSV file

#Note: The CSV file included in this explanation is just an example, there's no such as students.csv. You can search up and download actual datasets in CSV file format at kaggle.com 

import pandas as pd

# 1. Load the entire CSV file into a DataFrame table
df = pd.read_csv('students.csv')

# 2. Display the raw table
print("  Raw Data Table:  ")
print(df)
print("\n")

# 3. Do some basic data programming!
# Let's find the average grade of all students
average_grade = df['Grade'].mean()

print(f"The class average is: {average_grade}")

#prepared by: kai-cldece
