# Python Program to find the factors of a number
n = int(input("Enter any number: "))
for i in range(1,n+1):
    if n%i == 0:
        print(i)