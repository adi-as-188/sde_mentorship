class BankAccount:
    def __init__(self, account_holder, balance = 0.0):
        self.holder = account_holder
        self.balance = balance
        print(f"Account Created: {self.holder} - ${self.balance} | {id(self)}")

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
        else:
            print("Amount must be positive")

    def withdraw(self, amount):
        if amount >= 0:
            if self.balance >= amount:
                self.balance -= amount
            else:
                print("Insufficient funds")
        else:
            print("Amount must be positive")

    def display_balance(self):
        print(f"Bank Account: {self.holder} - ${self.balance}")


my_account = BankAccount("Aditya", 100.0)
print(id(my_account))
my_account.deposit(50)
my_account.withdraw(200)
my_account.withdraw(50)
my_account.display_balance()