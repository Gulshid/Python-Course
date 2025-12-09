# 3. Data Member and Member function
class Car:
    
    # Data Member 
    brand = ""
    year = 0
    
    # Member function
    def Model(self):
        print(f"Brand : {self.brand} year : {self.year}")


# class ==> object
c1 = Car()
c1.brand = "Toyota"
c1.year = 2020

c1.Model()
