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
