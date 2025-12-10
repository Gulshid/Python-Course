# Task 9: Make a class Employee and calculate yearly salary.
class Employee:
    # Constructor
    def __init__(self, name, monthly_salary):
        self.name = name
        self.monthly_salary = monthly_salary
        
    
    def yearly_Salary(self):
        return self.monthly_salary * 12
    

# object 
emp = Employee("Gulshid Zada", 45000)
print(f"The Name of Employee is : {emp.name} and his monthly Salary : {emp.monthly_salary}")
print(f"The Yearly Salary is : {emp.yearly_Salary()} of Employee : {emp.name}")