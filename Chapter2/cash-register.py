cost = int(float(input("What is the cost of the item? ")) * 100)
payment = int(float(input("How much cash are you paying? ")) * 100)
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1
change = payment - cost
change_quarters = change // QUARTER
change = change % QUARTER
print("Quarters", change_quarters)
change_dimes = change // DIME
change = change % DIME
print("Dimes ", change_dimes)
change_nickels = change // NICKEL
change = change % NICKEL
print("Nickels ", change_nickels)
change_pennies = change // PENNY
print("Pennies ", change_pennies)