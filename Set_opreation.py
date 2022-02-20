set1 = {"Apple", "banana", "chery", 1, 2, 3}
set2 = {1, 2, 3, 4, 5, 6, 7}

# The difference() method returns a set that contains the difference  between two sets.
print("Step--1\n")
set3 = set1.difference(set2)
print(set3)


# The difference_update() method removes the items that exist in both sets.
print("Step--2\n")
set1.difference_update(set2)
print(set1)


# The intersection() method returns a set that contains the similarity between two or more sets.
print("Step--3\n")
set1.update([1, 2, 3])
set4 = set1.intersection(set2)
print(set4)

# The intersection_update() method returns a set that contains the similarity between two or more sets.
print("Step--4\n")
set1.intersection_update(set2)
print(set1)

# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
print("Step--5\n")
set4 = set1.isdisjoint(set2)
print(set4)

# The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
print("Step--6\n")
set4 = set1.issubset()
print(set4)

# The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
print("Step--7\n")
set4 = set1.issuperset(set2)


