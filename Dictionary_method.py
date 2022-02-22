dict1 = {'Name': 'Ayaka', 'Age': 15, 'Class': 11}
dict2 = {'Name': 'Jean', 'Age': 17, 'Class': 12}
dict3 = {'Name': 'Xiao', 'Age': 18, 'Class': 'xxx'}
print(dict1)

# Dictionary Length
print("Dictionary length is: ", len(dict1))


# Adding Items in Dictionary
print("step--2\n")
dict1["Section"] = "A"
print(dict1)


# Removing Items in Dictionary

# The pop() method removes the item with the specified key name:
print("Step--3\n")
dict1.pop("Section")
print(dict1)


# The popitem() method removes the last inserted item
print("Step--4\n")
dict1.popitem()
print(dict1)

# The del keyword removes the item with the specified key name:
print("Step--5\n")
del dict2["Class"]
print(dict2)


# The del keyword can also delete the dictionary completely
print("Step--6\n")
del dict2


# The clear() method empties the dictionary
print("Step--7\n")
dict1.clear()
print(dict1)

# Copy a Dictionary

# built-in Dictionary method copy()
print("Step--8\n")
mydict = dict3.copy()
print(mydict)

# built-in function dict()
print("Step--9\n")
mydict1 = dict(dict3)
print(mydict1)


# Nested Dictionaries
print("Step--10\n")
dict4 ={"Studentdetails": {"Name": "Rosaria", "Age": 14, "Class": 10}}
print(dict4)

# Python Dictionary fromkeys() Method
print("step--11\n")
x = ("key1", "key2", "kay3")
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

# Python Dictionary update() Method
print("Step--12\n")
dict3.update({"Section": "A"})
print(dict3)