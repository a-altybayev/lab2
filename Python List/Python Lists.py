# Python List(Ordered, Changable, Allow Duplicates)
mylist = ['apple','banana','cherry']
print(mylist)

#Allow Duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#List lenght
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(thislist)) # 5

#List Items - Data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types:
list1 = ["xyz", 52, True, 40, "female"]

#type()
mylist = ["apple", "banana", "cherry"]
print(type(mylist)) # <class 'list'>

#The list() constructor
thislist = list(('apple','banana','cherry'))
print(thislist)