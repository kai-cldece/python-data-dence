#Control Flow. Machine decision making. 
#In order for the program to process the informtion and data it receives, the program must be able to make decision based on the data it receives.

#If and Else statements. These are the statements that make the program decide when the condition is met.
revenue = 5000
if revenue > 4000:
    print("Target met!")
else:
    print("Target missed.")

#For Loops. These are the conditions that automate repetitive tasks by iterating over a sequence. It is like a lkst of data.
prices = [10, 20, 30]
for price in prices:
    # Adds a 10% tax to each price
    print(price * 1.10)
