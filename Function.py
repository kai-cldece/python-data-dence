#In data analysis, we the programmers often calculate the same iteration for a hundred of times.   Instead of re-writing the code, we will be using the Function. 

# Defining the function
def calculate_profit(revenue, expenses):
    profit = revenue - expenses
    return profit

# Using the function later in your code
monday_profit = calculate_profit(500, 200)
print(monday_profit) # Output: 300