# Python Program to Find the Sum of Natural Numbers
n = int(input("Enter any Natural number: "))
sum = 0
if n > 0:
    for i in range(1,n+1):
       sum = sum + i
    print("Sum of {0} natural number: ".format(n), sum)