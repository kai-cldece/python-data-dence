"""
The task.
You have a temperature sensor outside your shop. Most of the time it works, but occasionally it glitches and records a temperature of -999. You need to clean this data before you can analyze it.

Objectives:
1. Create a list called raw_temps with these numbers: 72, 74, -999, 75, 71, -999, 73.
2. Create a new, empty list called clean_temps. (Hint: just use empty brackets []).
Write a for loop to iterate through raw_temps.
3. Inside the loop, write an if statement: If the temperature is not equal to -999, append (add) that temperature to your clean_temps list.
4. Print the clean_temps list. It should no longer contain any errors!

"""


# 1. A list containing multiple dictionaries
customers = [
    {"name": "Alice", "tier": "VIP", "spent": 150.00},
    {"name": "Bob", "tier": "Basic", "spent": 45.50},
    {"name": "Charlie", "tier": "VIP", "spent": 200.00}
]

# 2. Starting our counter at zero
vip_total = 0

# 3 & 4. Looping and checking conditions
for person in customers:
    # Remember to use == for checking equality!
    if person["tier"] == "VIP": 
        # Adding to the running total
        vip_total = vip_total + person["spent"] 

# 5. Output should be 350.0
print(f"Total VIP Revenue: ${vip_total}") 
