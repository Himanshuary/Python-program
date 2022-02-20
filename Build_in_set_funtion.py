import math
set1 = {"Apple", "banana", "chery",}
set2 = {10, 20, 30, 40, 50}
print(set1)

# using add() method we can add a value in set
print("Step--1\n")
set1.add("Orange")
print(set1)

# using update() method we can add multiple value in set
print("Step--2\n")
set1.update(["Mango", "Grapes"])
print(set1)

# Using len() method we can get no of item in set
print("Step--2\n")
print("No of item in set: ", len(set1))

# using remove() method we can remove a value in set
print("Step--3\n")
set1.remove("banana")
print(set1)

# using discard() method we can remove a value in set
print("Step-4\n")
set1.discard("Orange")
print(set1)

# Using pop() method removes a random item from the set.
print("Step--5\n")
set1.pop()
print(set1)

# Using union() we can join two set.
print("Step--6\n")
set3 = set1.union(set2)
print(set3)

# Using update() we can join two set.
print("Step--7\n")
set1.update(set2)
print(set1)

# Using copy() we can copy a set.
print("Step--8\n")
x = set2.copy()
print("Copy set: ", x)

