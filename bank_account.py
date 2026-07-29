class InsufficientFundsError(Exception):
    pass


class NegativeAmountError(Exception):
    pass


class BankAccount:
    def __init__(self, account_holder, balance = 0.0):
        self.holder = account_holder
        self.__balance = balance
        print(f"Account Created: {self.holder} - ${self.__balance} | {id(self)}")

    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError("Cannot process negative amounts.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError("Cannot process negative amounts.")
        if self.__balance < amount:
            raise InsufficientFundsError("Not enough money in the account.")
        self.__balance -= amount

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


my_account = BankAccount("Aditya Robust", 100)

try:
    print("Attempting to withdraw $200...")
    my_account.withdraw(200) # This should trigger the exception
    print("Withdrawal successful!") # This line will NEVER run
    
except InsufficientFundsError as e:
    print(f"BANK ALERT: {e}")
    
except NegativeAmountError as e:
    print(f"BANK ALERT: {e}")
    
except Exception as e:
    # A generic catch-all for any other weird bugs we didn't foresee
    print(f"CRITICAL SYSTEM FAILURE: {e}")

print("Program continues running smoothly because we caught the error...")