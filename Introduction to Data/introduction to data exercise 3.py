"""
The task.
You run a subscription service. You have a list containing the data of three customers. You need to write a script that calculates the total amount of money spent only by your "VIP" customers.

Objectives:
1. Create a list named customers. Inside this list, place three dictionaries. Each dictionary should have three keys: "name", "tier", and "spent".
Customer 1: Name: "Alice", Tier: "VIP", Spent: 150.00
Customer 2: Name: "Bob", Tier: "Basic", Spent: 45.50
Customer 3: Name: "Charlie", Tier: "VIP", Spent: 200.00
2. Create a variable called vip_total and set it to 0. (This will hold our running total).
3. Write a for loop to check each customer in the list.
4. Inside the loop, use an if statement: If the customer's "tier" is exactly equal to "VIP", add their "spent" amount to your vip_total variable.
5. Finally, print the vip_total.
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
