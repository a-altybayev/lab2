# Set - unchangable, unordered, unindexed, duplicates NOT allowed
thisset = {"apple", "banana", "cherry"}
print(thisset)

# True and 1 is considered the same value:
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

# False and 0 is considered the save value:
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)

# Get the lenght of a set
thisset = {"apple", "banana", "cherry"}
print(len(thisset))

# Set Items - Data types
set1 = {"abc", 34, True, 40, "male"}

# type() - <class 'set'>

# The set() constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
