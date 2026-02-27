# Day 04: Practicing numbers and mathematical operations

# We'll start our bill at zero and update it as we go.
running_total = 0

# Setting the number of people to split the final cost with.
num_of_friends = 4

# These are our individual costs. In Python, these decimals are called "floats."
appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

# Let's sum up all the items to get our subtotal.
running_total = appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

# Calculating a 25% tip. Multiplying by 0.25 is the easiest way to find a percentage.
tip = running_total * 0.25
print('Tip amount:', tip)

# We use += to "add and assign," effectively adding the tip into our running total.
running_total += tip
print('Total with tip:', running_total)

# Now, we divide the grand total by the number of friends.
final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

# Division often creates long decimals (like .72222). 
# Using round( , 2) ensures it looks like actual money with only two decimal places.
each_pays = round(final_bill, 2)
print("Each person pays:", each_pays)
