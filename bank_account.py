class BankAccount:
    def __init__(self, account_holder, balance = 0.0):
        self.holder = account_holder
        self.__balance = balance
        print(f"Account Created: {self.holder} - ${self.__balance} | {id(self)}")

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
        else:
            print("Amount must be positive")

    def withdraw(self, amount):
        if amount >= 0:
            if self.__balance >= amount:
                self.__balance -= amount
            else:
                print("Insufficient funds")
        else:
            print("Amount must be positive")

    def display_balance(self):
        print(f"Bank Account: {self.holder} - ${self.__balance}")

    def get_balance(self):
        return self.__balance


secure_account = BankAccount("Aditya", 500)

# 1. Try to hack the bank (this will fail to change the actual balance)
secure_account.__balance = 1000000

# 2. Print the REAL balance using your getter method
print(f"Real Balance: {secure_account.get_balance()}")