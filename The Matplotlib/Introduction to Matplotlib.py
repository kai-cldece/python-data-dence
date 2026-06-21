# INTRODUCTION TO MATPLOTLIB
# Matplotlib is Python's core data visualization library.
# While Pandas helps us filter and analyze data, Matplotlib helps us
# actually SEE the trends by creating charts and graphs.

# Step 1: Import the library
# We import a specific module called 'pyplot' which is designed for 
# plotting charts, and we give it the universal nickname 'plt'.
import matplotlib.pyplot as plt

# Let's create some simple mock data 
# (In a real scenario, you would extract these lists from your Pandas DataFrame!)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
revenue = [150, 200, 180, 250, 300]


# EXAMPLE 1: Creating a Basic Line Chart
print("Generating Line Chart...")

# The .plot() function creates a standard line graph. 
# The first argument is the X-axis (bottom), the second is the Y-axis (side).
plt.plot(days, revenue, marker='o', color='blue') 
# (Added 'marker' to show dots on the data points)

# A chart is useless without labels! Let's add them:
plt.title("Coffee Shop Revenue Over the Week")
plt.xlabel("Days of the Week")
plt.ylabel("Revenue in USD ($)")

# The .show() command is crucial. It tells Python to actually open a 
# window and display the graphic you just built.
plt.show()

# EXAMPLE 2: Creating a Bar Chart
print("Generating Bar Chart...")

# The .bar() function works exactly like .plot(), but creates columns.
plt.bar(days, revenue, color='skyblue')

# Adding our labels for this new chart
plt.title("Coffee Shop Revenue (Bar Chart)")
plt.xlabel("Days of the Week")
plt.ylabel("Revenue in USD ($)")

# Display the bar chart
plt.show()

# IMPORTANT NOTE FOR THE PROGRAMMERS: 
# When running this script, the code pauses on the first 'plt.show()'. 
# You have to close the first pop-up window before the bar chart will appear!
