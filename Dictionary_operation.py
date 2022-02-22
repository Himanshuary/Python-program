dict1 = {'Name': 'Ayaka', 'Age': 15, 'Class': 11}
dict2 = {'Name': 'Jean', 'Age': 17, 'Class': 12}
dict3 = {'Name': 'Xiao', 'Age': 18, 'Class': 'xxx'}
print(dict1)

# Change Values in Dictionary
dict1["Name"] = 'Kokomi'
print(dict1)

# Loop Through a Dictionary

# 1. Print all key names in the dictionary, one by one
print("Step--2\n")
for i in dict1:
    print(i)

# 2. Print all values in the dictionary, one by one:
print("Step--3\n")
for i in dict1:
    print(dict1[i])

# 3. You can also use the values() method to return values of a dictionary:
print("Step--4\n")
for i in dict1.values():
    print(i)

# 4. Loop through both keys and values, by using the items() method:
print("Step--5\n")
for x, y in dict1.items():
    print(x, y)
# Check if Key Exists in Dictionary
print("Step--6\n")
if "Name" in dict1:
    print("Yes 'Name' is a key in dict1")
