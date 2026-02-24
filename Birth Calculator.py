#birthCalculator() function to count current age of person
def birthCalculator(curr, birth):
    current_age=(curr - birth)
    print("Hey ", name, " .Your current age is: ", current_age)
   #Displaying message on the basis of current age
    if(current_age>=18):
     print("You are an adult!")
    else:
     print("You are minor!")
#name variable which takes input from user and displays  
name=input("What is your name?")
print("hello ", name)
#birth_year variable which takes input from user in int datatype and stores
birth_year=(int(input("What is your Birth Year?")))
current_year=2026
#calling the function to calculate age
birthCalculator(current_year, birth_year)
