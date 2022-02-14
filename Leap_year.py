#Python Program to Check Leap Year
year = int(input("Enter any year: "))
if ((year%4==0) or (year%100!=0)) and (year%400==0):
    print("{0} is a leap year")
else:
    print("{0} is a not leap year")
        