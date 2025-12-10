# Task 2: Create a class Student with constructor and a method show().
class Student:
    
    # constructor
    def __init__(self):
        self.name = input("Enter your Name :")
        self.age = int(input("Enter your Age :"))
        
        
    # def __init(self, name, age):
    #     self.name = name
    #     self.age = age
        
    # show function
    def show(self):
        print(f"Student Name : {self.name}.    Age : {self.age}")
        
        

# object
# method 1
# s1 = Student("Gulshid Zada", 23)
# s2 = Student("Muhammad", 22)
# s1.show()
# s2.show()

# method 2
s3 = Student()
s3.show()