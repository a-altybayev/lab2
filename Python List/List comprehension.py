# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
#or
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

"""
The Syntax
newlist = [expression for item in iterable if condition == True]
"""


# Condition
newlist = [x for x in fruits if x != "apple"]


# Iterable
newlist = [x for x in range(10)]
#or
newlist = [x for x in range(10) if x < 5]

# Expression
newlist = [x.upper() for x in fruits]

newlist = ['hello' for x in fruits]

newlist = [x if x != "banana" else "orange" for x in fruits]
#Return the item if it is not banana, if it is banana return orange