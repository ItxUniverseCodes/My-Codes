# Day 05: Practicing Boolean and Conditionals(if, elif, else)
# --- Setup ---
base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'
is_member = False
is_weekend = False

# --- Age Verification ---
# Simple check for general entry
if age > 17:
    print('User is eligible to book a ticket')

# Check for specific 'Evening' show age restrictions
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

# --- Discounts & Surcharges ---
# Membership discount requires being a member AND meeting the age gate
discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

# Apply extra charges if it's the weekend OR an evening show
extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

# --- Final Booking Logic ---
# Complex logic: User must be 21+ OR (18+ and meeting time/membership rules)
if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    # Nested check: Determine service fee based on seat tier
    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)  

    # Final math: Combine all factors into the final total
    final_price = base_price + extra_charges + service_charges - discount 
    print("Final price of ticket:", final_price) 
else:
    # This runs if the complex logic above evaluates to False
    print('Ticket booking failed due to restrictions')
