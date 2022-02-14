#Python Program to Solve Quadratic Equation
import cmath
def Quadraticequatin(a,b,c):
    d = (b**2)-(4*a*c)
    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)
    print("Given Quadratic equation is: %ix + %iy + %i = 0"%(a,b,c))
    print("Root is: ",sol1,sol2)
Quadraticequatin(2,4,6)
    
    