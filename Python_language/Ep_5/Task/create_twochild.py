# Task 14: Create two child classes overriding start().
class Base:
    def start(self):
        pass
    


class Car(Base):
    def start(self): # method overrding
        print("Car is start ===>")
        

class Bike(Base):
    def start(self): # method overrding
        print("Bike is start ===>")
        
# object 
c = Car()
b = Bike()

c.start()
b.start()