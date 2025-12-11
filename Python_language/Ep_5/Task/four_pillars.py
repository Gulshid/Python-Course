# Task 15: Make one program showing all four OOP pillars.
# Encapsulation
class Encapsulation:
    # Constructor function
    def __init__(self, balance):
        self.__balance = balance # => Private Access Specifier (Encapsulation)
    
    def get_balance(self):
        return self.__balance
    
    def deposite(self, amount):
        self.__balance = amount
        

# Inheritence
class Animal:
    def sound(self):
        print("Animal Make Sound")
        

class Dog(Animal):
    def sound(self):
        print("Dog barks")
    

# polymorphism
def set_value(a):
    a.sound()
    
# Abstraction 
class Calculator:
    def add(self, x, y):
        return x + y

# Object 
# Encapsulation
en = Encapsulation(1200)
print("Current Balance :",en.get_balance())

en.deposite(3400)
print("Current Balance :",en.get_balance())


# Inheritence  +  Polymorphism
d = Dog()
a = Animal()

set_value(d)
set_value(a)

# Abstraction
cal = Calculator()
print("The addition of two value is :", cal.add(4,6)) # Abstraction


