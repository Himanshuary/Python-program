# Python Program to Check Prime Number
n = int(input("Enter any number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("{0} is not a prime number".format(n))
            break
    else:
        print("{0} is a prime number".format(n))
else:
    print("{0} is not a prime number".format(n))
