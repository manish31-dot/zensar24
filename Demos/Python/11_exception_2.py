print("EMPLOYEE SALARY CALCULATOR")

try:

    salary = 50000

    bonus = "5000"

    total_salary = salary + bonus

    print("Total Salary:", total_salary)
# if there is not type conversion it means that is TypeError 
except TypeError:

    print("Cannot perform operation on incompatible data types.")