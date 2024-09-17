# Python For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Looping Through a String
for x in "banana":
  print(x)

# The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
# The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# The range() Function
for x in range(9):
  print(x)

for x in range(4,12):
  print(x)

for x in range(4,12,3):
  print(x)


# Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")


# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# The pass Statement - to avoid getting an error

for x in [0, 1, 2]:
  pass