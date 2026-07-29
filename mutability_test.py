# --- TESTING IMMUTABILITY (Strings) ---
my_string = "Hello"
print(f"Original String: {my_string} | Address: {id(my_string)}")

# We "modify" the string by adding to it
my_string = my_string + " World"
print(f"Modified String: {my_string} | Address: {id(my_string)}\n")


# --- TESTING MUTABILITY (Lists) ---
my_list = [1, 2, 3]
print(f"Original List: {my_list} | Address: {id(my_list)}")

# We modify the list in place using .append()
my_list.append(4)
print(f"Modified List: {my_list} | Address: {id(my_list)}")