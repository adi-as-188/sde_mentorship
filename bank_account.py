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


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.deposit(self.get_balance() * self.interest_rate)


# Create a Savings Account with 5% interest
my_savings = SavingsAccount("Aditya", 1000, 0.05)

# Display initial balance
my_savings.display_balance()

# Apply interest
my_savings.apply_interest()

# Display new balance (Should be 1050)
my_savings.display_balance()