class Employee:
    def __init__(self,name,age,salary,gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def show_employee_details(self):
        print("Name of employee is: ",self.name)
        print("Age of employee is: ",self.age)
        print("Salary of employee is: ",self.salary)
        print("Gender of employee is: ",self.gender)

e1 = Employee("Rohan Saini", 20, 120000, "Male")
e1.show_employee_details()



