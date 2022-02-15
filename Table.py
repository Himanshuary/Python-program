# Python Program to Display the multiplication Table

n = int(input("Enter any number: "))
Table = 1
for i in range(1, 11):
    Table = n*i
    print("Table of {0} is: ".format(n), Table)