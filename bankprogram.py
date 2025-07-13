# let's create a program where we have to create a similar application like atm
# Requirements :-- username, userpin, account-type,branch-code
# If user's account is saving then amount=1000 and if current then amount will be 5000
# user can change pin and can withdraw amount which will automatically update in main amount
# user can add money to account too

# opts(options)


import datetime 
from datetime import datetime

# Initialization
now = datetime.now()
print("Welcome to the ATM service from Central Bank of India")
print("Date:", now.date(), "Time:", now.time())
print("-----------------------------------------------------")

# User Details
username = "Manan Chawla"
userpin = 1234
branchcode = 2580

# Account Setup
Account_type = input("Enter your account type (c for current / s for saving): ").lower()
if Account_type == 'c':
    amount = 5000
else:
    amount = 1000

print(f"\nWelcome Mr. {username} to the ATM service")
print(f"Your account type is: {'Current' if Account_type == 'c' else 'Saving'}")
print(f"Your total balance is: ₹{amount}")

# ATM Menu Loop
while True:
    print("\nATM SERVICES:")
    print("1. Withdraw amount")
    print("2. Change PIN")
    print("3. Check balance")
    print("4. Add money")
    print("5. Exit application")

    option = input("Choose the option to proceed (1-5): ")

    if option == "1":
        withdraw_amount = int(input("Enter amount to withdraw: "))
        if withdraw_amount > amount:
            print(" Insufficient balance!")
        else:
            amount -= withdraw_amount
            print(f" Amount withdrawn successfully. Remaining balance: ₹{amount}")

    elif option == "2":
        entered_code = int(input("Enter your branch code to change PIN: "))
        if entered_code == branchcode:
            userpin = int(input("Enter new PIN: "))
            print(" PIN changed successfully.")
        else:
            print(" Incorrect branch code!")

    elif option == "3":
        print(f" Your current balance is: ₹{amount}")

    elif option == "4":
        deposit = int(input("Enter amount to add: "))
        amount += deposit
        print(f" ₹{deposit} added successfully. New balance: ₹{amount}")

    elif option == "5":
        print("Thank you for visiting the Central Bank of India ATM service.")
        break

    else:
        print("⚠ Invalid option! Please try again.")
