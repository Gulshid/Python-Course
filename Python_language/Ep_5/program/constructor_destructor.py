# Constructor and Destructor
class Student:
    
    # Constructor
    def __init__(self):
        print("Name and Age is Created ")
        self.name = input("Enter your Name :")
        self.age = int(input("Enter your Age :"))
        
        
    
    
    def display(self):
        print(f"Name : {self.name} Age : {self.age}")
        
    
    # Destructor
    def __del__(self):
        print(f"Name : {self.name} Destroyed ")
        

# class ==> object
stud = Student()
stud.display()
