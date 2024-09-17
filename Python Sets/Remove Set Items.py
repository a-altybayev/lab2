# Remove Item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# discard()
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# pop()
thisset = {"apple", "banana", "cherry"}
x = thisset.pop() # removes a random item
print(x)
print(thisset)
# clear()
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# del
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)