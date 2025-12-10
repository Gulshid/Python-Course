# Task 3: Create two classes Animal and Dog to show inheritance.
class Animal:
    def sound(self):
        print("Animal Makes a Sound...")
    
    

class Dog(Animal):
    def barks(self):
        print("Dogs barks ...")
        
        

# object
d = Dog()
d.sound()

d.barks()
    