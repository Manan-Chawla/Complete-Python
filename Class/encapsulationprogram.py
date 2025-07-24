class Banks:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number 
        self.__balance = initial_balance    

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self): 
        return self.__balance

# Usage
b1 = Banks("123456789", 1000)

b1.deposit(500)
b1.withdraw(200)
b1.withdraw(1500) # Insufficient funds
print(f"Current balance: {b1.get_balance()}")
