import time

print("Buidling massive list and set... (This might take a few seconds)")

# We create a list of 10 million numbers
# We use a trick called a "Generator" (range) to do this cleanly
elements = 10_000_000

massive_list = list(range(elements))
massive_set = set(range(elements))

target = 9_999_999 # The very last number, the worst-case scenario!

print("Data structures built. Starting the race...\n")

# --- RACE 1: THE LIST O(N) ---
start_time = time.time()
result = target in massive_list # This forces Python to search
end_time = time.time()

list_time = end_time - start_time
print(f"List Search Time: {list_time:.5f} seconds")


# --- RACE 2: THE SET O(1) ---
start_time = time.time()
result = target in massive_set # This forces Python to hash and jump
end_time = time.time()

set_time = end_time - start_time
print(f"Set Search Time: {set_time:.5f} seconds")

# --- RESULTS ---
print(f"\nThe Set was roughly {list_time / set_time:,.0f} times faster!")