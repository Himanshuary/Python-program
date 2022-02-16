# how to use lambda filter map and reduce function
from functools import reduce
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter
even = list(filter(lambda n : n%2 == 0, list1))
print(even)

# map
double = list(map(lambda n : n*2 , even))
print(double)

# reduce
Sum = reduce(lambda a,b : a+b,double)
print(Sum)
