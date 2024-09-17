# Loop Through a Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# Print all key names in dictionary: 
for x in thisdict:
  print(x)

# Print all VALUES in the dictionary:
for x in thisdict:
  print(thisdict[x])
#or
for x in thisdict.values():
  print(x)

#Print the keys by .keys()
for x in thisdict.keys():
  print(x)

# Print both keys and values .items():
for x, y in thisdict.items():
  print(x, y)