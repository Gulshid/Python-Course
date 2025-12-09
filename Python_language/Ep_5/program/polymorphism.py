# polymorphism
class Animal:
    def sound(self):
        print("Animal Makes a Sound")
        


class Dogs(Animal):
    def sound(self):
        print("Dogs barks")


# class ===> object
d = Dogs()
d.sound()
Animal.sound(d)
        
        

