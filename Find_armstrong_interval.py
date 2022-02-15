# Python Program to Find Armstrong Number in an Interval
lower = 100
upper = 2000
for i in range(lower,upper+1):
    order = len(str(i))
    x = i
    r = 0
    while i>0:
        a = i%10
        r = r + a**order
        i=i//10
    if x == r:
        print("{0} is a armstrong number".format(x))


