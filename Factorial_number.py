# Python Program to Find the Factorial of a Number
n = int(input("Enter any number: "))
fact = 1
for i in range(1, n+1):
    fact = fact*i
print("factorial of {0} is: ".format(n), fact)