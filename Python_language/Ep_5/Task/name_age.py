# Task 11: Create a class with constructor that sets name & age.
class Person:
    # Constructor function 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    
    # display name age 
    def display(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")


# object 
per = Person("Muhammad ", 23)
per.display()
print("************")
per = Person("Gulshid Zada ", 25)
per.display()

        