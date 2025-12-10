# Task 1: Create a class Car with data members: brand, model. Add a function to display details.
class Car:
    brand = "Toyota Carrola"
    model = 2023
    
    def display_detail(self):
        print(f"Brand : {self.brand}.  Model : {self.model}")
        


# object
car = Car()
car.display_detail()


print(f"{Car.brand}. {Car.model}")