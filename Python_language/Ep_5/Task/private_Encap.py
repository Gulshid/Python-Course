# Task 7: Demonstrate encapsulation using a private variable (__balance).
class Wallet:
    
    # Constructor 
    def __init__(self, balance):
        self.__balance = balance #  ===> Encapsulation __balance use
        
    
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            
            
# object 
w = Wallet(450)
print("The  Amount :", w.get_balance())


w.set_balance(500)
print("The Amount :", w.get_balance())
            
