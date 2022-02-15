# Python Program to Print all Prime Numbers in an Interval
lower = 900
upper = 1000
print("Prime number between {0} to {0} is".format(lower,upper))
for i in range(lower, upper+1):
    if i > 1:
        for num in range(2, i):
            if i%num == 0:
                break
        else:
            print(i)

