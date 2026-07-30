import sys

def list_transactions(limit):
    transactions = []
    for i in range(1, limit+1):
        transactions.append(f"TRANSACTION ID: {i}")
    return transactions


def yield_transactions(limit):
    for i in range(1, limit+1):
        yield f"TRANSACTION ID: {i}"


# We are going to simulate 10 Million transactions
limit = 10_000_000

print("Generating List...")
# This will take a few seconds and consume massive RAM
massive_list = list_transactions(limit)
print(f"List Size in Memory: {sys.getsizeof(massive_list):,} bytes")

print("\nGenerating Generator")
massive_generator = yield_transactions(limit)
print(f"Generator Size in Memory: {sys.getsizeof(massive_generator):,} bytes")

# To prove the generator works, let's manually ask for the first 3 items using the built-in next() function!
print("\nProcessing first 3 transactions from the generator:")
print(next(massive_generator))
print(next(massive_generator))
print(next(massive_generator))