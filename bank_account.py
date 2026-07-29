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

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account[{self.holder}] - Balance: ${self.get_balance()}"


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.deposit(self.get_balance() * self.interest_rate)


class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, transaction_fee = 1.00):
        super().__init__(account_holder, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount):
        super().withdraw(amount + self.transaction_fee)


# 1. Test Dunder Method
my_account = BankAccount("Aditya Default", 500)
print(my_account)

# 2. Test Checking Account Polymorphism
my_checking = CheckingAccount("Aditya Checking", 100)
my_checking.withdraw(20) # Withdrawing 20, but it should deduct 21!
print(my_checking)