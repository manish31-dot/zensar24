print("STUDENT AGE VALIDATION")

try:

    age = int(input("Enter Age: "))

    print("Age Entered:", age)
# if there is type conversion it means that is value error
except ValueError:

    print("Invalid Input.")
    print("Please enter numeric values only.")

print("Application Ended")