# Accessing Items
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
#or
x = thisdict.get("model")
print(x)


# Get Keys
x = thisdict.keys()
print(x) # dict_keys(['brand', 'model', 'year']) 


# Get Values
x = thisdict.values()
print(x) # dict_values(['Ford', 'Mustang', 1964])


# Get Items
x = thisdict.items()
print(x) # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

