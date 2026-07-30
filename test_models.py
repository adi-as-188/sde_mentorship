import pytest
from models import BankAccount, SavingsAccount, CheckingAccount, InsufficientFundsError, NegativeAmountError

# Test 1: Does the account initialize correctly?
def test_bank_account_initializationn():
    account = BankAccount("Test User", 100.0)
    assert account.holder == "Test User"
    assert account.get_balance() == 100.0

# Test 2: Does the deposit math work?
def test_ban_account_deposit():
    account = BankAccount("Test User", 100.0)
    account.deposit(50.0)
    assert account.get_balance() == 150.0

# Test 3: Does our custom Exception actually trigger?
def test_negative_deposit_raises_error():
    account = BankAccount("Test User", 100.0)

    # 'pytest.raises' forces the test to PASS if the specific error is raised!
    with pytest.raises(NegativeAmountError):
        account.deposit(-50.0)