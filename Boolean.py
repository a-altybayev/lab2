# Boolean values
# Ex.1
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Ex.2
a = 210
b = 333
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") # b is greater than a


# Evaluate Values and Variables
# Ex.4 
print(bool("Hello")) #True
print(bool(15)) #True

# Ex.5
x = "Hello"
y = 10
print(bool(x)) #True
print(bool(y)) #True


# Some Values are true
# Almost any value is evaluated to TRUE if it has some sort of content.
bool("abc")
bool(123)
bool(['apple','cherry','banana'])


# Some values are false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# Functions can return a boolean
# Ex.6
def myfunc():
  return True
print(myfunc())

# Ex.7
def myfunc():
  return True
if myfunc():
  print ("TRUE")
else:
  print("NO!")

# Ex.8
x = 200
print(isinstance(x))