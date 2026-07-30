from models import InsufficientFundsError, NegativeAmountError, audit_logger, BankAccount, SavingsAccount, CheckingAccount

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