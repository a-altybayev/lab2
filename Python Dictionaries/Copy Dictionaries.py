# Copy a Dictionary
'''You cannot copy a dictionary simply by typing dict2 = dict1,
because: dict2 will only be a reference to dict1,
and changes made in dict1 will automatically also be made in dict2.
'''
# .copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)