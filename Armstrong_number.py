# Python Program to Check Armstrong Number
n = int(input("Enter any number: "))
r = 0
x = n
while n > 0:
    a = n%10
    r = r + a**3
    n = n//10

if x == r:
    print("{0} is a armstrong number".format(x))
else:
    print("{0} is a not armstrong number".format(x))