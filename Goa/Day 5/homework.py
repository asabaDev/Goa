# Ask the user for their salary
salary = int(input("Enter your salary: "))

# If it's greater than 10,000, print "Are you studying at GOA?"
if salary > 10000:
    print("Are you studying at GOA?")

# If it's between 1,000 and 10,000, print "you mid"
elif 1000 <= salary <= 10000:
    print("you mid")

# If it's less than 1,000, print "Welcome to GOA, Matrix!"
elif salary < 1000:
    print("Welcome to GOA, Matrix!")
