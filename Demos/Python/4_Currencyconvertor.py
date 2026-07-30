print("Currency Converter")
print("1. Dollar to Rupees")
print("2. Rupees to Dollar")

current_dollor_rate = 95.60

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    dollars = float(input("Enter amount in Dollars: "))
    rupees = dollars * current_dollor_rate  # Example exchange rate
    print("Amount in Rupees =", rupees)

elif choice == "2":
    rupees = float(input("Enter amount in Rupees: "))
    dollars = rupees / current_dollor_rate  # Example exchange rate
    print("Amount in Dollars =", round(dollars, 2))

else:
    print("Invalid Choice")