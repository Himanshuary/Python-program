# Python Program to Find LCM
a = 5
b = 4
for i in range(1, (a*b)+1):
    if i%a == 0 and i%b == 0:
        print("LCM of number is: ", i)
        break
        