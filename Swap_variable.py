#Python Program to Swap Two Variables

# first method

a = 2
b = 4
print("Variable is: ",a,b)
c = a
a = b
b = c
print("swap: ",a,b)

# Second method
def swap(a,b):
    print("Variable is: ",a,b)
    a,b=b,a
    print("swap: ",a,b)
swap(10,20)

