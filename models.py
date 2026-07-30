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
    def __init__(self, account_holder: str, balance: float = 0.0):
        self.holder = account_holder
        self.__balance = balance
        print(f"Account Created: {self.holder} - ${self.__balance} | {id(self)}")

    @audit_logger
    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise NegativeAmountError("Cannot process negative amounts.")
        self.__balance += amount
        self.log_transaction("Deposited", amount)

    @audit_logger
    def withdraw(self, amount: float) -> None:
        if amount < 0:
            raise NegativeAmountError("Cannot process negative amounts.")
        if self.__balance < amount:
            raise InsufficientFundsError("Not enough money in the account.")
        self.__balance -= amount
        self.log_transaction("Withdrew", amount)

    def get_balance(self) -> float:
        return self.__balance

    def __str__(self) -> str:
        return f"Account[{self.holder}] - Balance: ${self.get_balance()}"

    def log_transaction(self, action: str, amount: float) -> None:
        with open(f"{self.holder}_ledger.txt", "a") as file:
            file.write(f"{action}: ${amount} | New Balance: {self.get_balance()}\n")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, balance: float = 0, interest_rate: float = 0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        self.deposit(self.get_balance() * self.interest_rate)


class CheckingAccount(BankAccount):
    def __init__(self, account_holder: str, balance: float = 0, transaction_fee: float = 1.00):
        super().__init__(account_holder, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount: float) -> None:
        super().withdraw(amount + self.transaction_fee)
