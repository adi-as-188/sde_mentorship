class InsufficientFundsError(Exception):
    pass


class NegativeAmountError(Exception):
    pass


def audit_logger(func):
    def wrapper(*args, **kwargs):
        print(f"[AUDIT LOG] Executing {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"[AUDIT LOG] {func.__name__} execution complete.")

        return result

    return wrapper


class BankAccount:
    def __init__(self, account_holder, balance = 0.0):
        self.holder = account_holder
        self.__balance = balance
        print(f"Account Created: {self.holder} - ${self.__balance} | {id(self)}")

    @audit_logger
    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError("Cannot process negative amounts.")
        self.__balance += amount
        self.log_transaction("Deposited", amount)

    @audit_logger
    def withdraw(self, amount):
        if amount < 0:
            raise NegativeAmountError("Cannot process negative amounts.")
        if self.__balance < amount:
            raise InsufficientFundsError("Not enough money in the account.")
        self.__balance -= amount
        self.log_transaction("Withdrew", amount)

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account[{self.holder}] - Balance: ${self.get_balance()}"

    def log_transaction(self, action, amount):
        with open(f"{self.holder}_ledger.txt", "a") as file:
            file.write(f"{action}: ${amount} | New Balance: {self.get_balance()}\n")


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


my_account = BankAccount("Aditya Decorator", 500)
my_account.deposit(100)
my_account.withdraw(50)