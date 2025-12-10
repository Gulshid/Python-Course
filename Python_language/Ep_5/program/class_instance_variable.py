# 11.Instance Variables vs Class Variables
class Car:
    wheel = 4  # Class variable
    def Num(self, color):
        self.color = color # instance variable
        return self.color


# class ===> object
c1 = Car()
print("the Color of Car is :", c1.Num("Red"))

print("the wheel of car is :", Car.wheel)
print("**********")

print("the Color of Car is :", c1.Num("Blue"))
print("the wheel of car is :", Car.wheel)
        