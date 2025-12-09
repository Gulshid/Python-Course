# Encapsulation
class Person:
    def __init__(self, name, age):
        # Encapsulation
        self.name = name
        self._age = age
        self.__salary = 15000
        
    
    
    def display(self):
        print(f"Name : {self.name}.  Age : {self._age}.  Salary :{self.__salary}")
        
        


# class ==> object 
person = Person("Gulshid Zada", 23)
person.display()
