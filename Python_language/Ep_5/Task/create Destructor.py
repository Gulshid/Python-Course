# Task 12: Create a destructor that prints “Destroyed”.
class Destructor:
    def __del__(self):
        print("*** Destructor function ***")
        print("Destroyed")

# object 
des = Destructor()
