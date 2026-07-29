import sys

# 1. Create an object and a label
a = 10500
print(f"Memory Address of 'a' (10500): {id(a)}")

# 2. Point a new object to that exact same object
b = a
print(f"Memory Address of 'b' (10500): {id(b)}")

# 3. Check the reference count of the object 10500
# (Note: getrefcount adds a temporary +1 to the count just by running)
ref_count = sys.getrefcount(a)
print(f"Reference Count for the object 10500: {ref_count}")

# 4. Change 'a' and see what happens to the memory address
a = 10501
print(f"New Mempry Address of 'a' (10501): {id(a)}")
print(f"Memory Address of 'b' (is it still 10500?): {id(b)}")