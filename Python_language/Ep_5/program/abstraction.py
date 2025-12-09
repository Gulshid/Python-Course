# 5. Abstraction 
class CoffeeMachine:
    def make_coffee(self):
        print("Making a Coffee ...")
        self._boil_water()
        
        
    def _boil_water(self):
        print("Water is Boiling...")
        

# class ==> object
# Abstraction
coffee = CoffeeMachine()
coffee.make_coffee()