# Task 6: Create a class Rectangle to calculate area and perimeter.
class Rectangle:
    
    # Constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    

# object 
rec = Rectangle(4,3)

print("The Area of Rectangle is :", rec.area())
print("The Perimeter of Rectangle is :", rec.perimeter())
