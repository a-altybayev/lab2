# Python Conditions and IF statements
"""
Python Conditions and If statements
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""
# Example
a = 222
b = 892
if b > a:
  print("b is greater than a")


# Elif statement = else if()
# Example
a = 123
b = 123
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


# Else statement
a = 20
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# Short Hand If
if a < b: print("b is greater than a")


# Short Hand If ... Else 
a = 0
b = 30
print("A") if a > b else print("B")


# And
a = 20
b = 33
c = 10
if a > b and c > a:
  print("Both conditions are True")


# Or 
a = 20
b = 33
c = 10
if a > b or a > c:
  print("At least one of the conditions is True")


# Not
a = 3
b = 20
if not a > b:
  print("a is NOT greater than b")


# Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")


# The pass Statement