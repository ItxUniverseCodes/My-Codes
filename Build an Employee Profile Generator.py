# First, let's set up the basic identity. 
# We're combining the first and last name with a space so it looks natural.
first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name

# I'm using += here to "tack on" the apartment number to the original address.
address = '123 Main Street'
address += ', Apartment 4B'

# Since age is a number, we have to wrap it in str() to "talk" to the text.
# Otherwise, Python gets confused trying to add numbers and words together.
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

years_experience = 5
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

# F-strings (the 'f' before the quotes) are a lifesaver. 
# They let us drop variables directly into a sentence using curly braces {}.
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

# Now for the "Data Surgery" (String Slicing).
# We're pulling specific pieces out of a standardized ID code.
employee_code = 'DEV-2026-JD-001'

# Grabbing the first three letters—this tells us the department.
department = employee_code[0:3]
print(department)

# Pulling out the year of hiring (characters 4 through 7).
year_code = employee_code[4:8]
print(year_code)

# Snagging the initials from the middle of the string.
initials = employee_code[9:11]
print(initials)

# Using a negative index [-3:] is a pro move—it just means "grab the last 3 characters."
last_three = employee_code[-3:]
print(last_three)
