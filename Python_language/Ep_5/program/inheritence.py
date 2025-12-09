# Inheritence
class mul:
    def multiply(self):
        self.x = int(input("Enter the value for x :"))
        self.y = int(input("Enter the value for y :"))
        
        print(f"The multiplication of two value is : {self.x * self.y}")
        

class divide(mul):
    def div(self):
        self.a = int(input("Enter the value for a :"))
        self.b = int(input("Enter the value for b :"))
        
        print(f"The division of two value is : {self.a / self.b}")



# class ===> object
mu = divide()
mu.multiply()
mu.div()