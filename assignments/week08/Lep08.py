"""
Write a Python class Rectangle with:

Private attributes for length and width
Methods to calculate area (getArea()) and perimeter getPerimeter())
A method to check if it's a square (isSquare())

"""

#Code 1

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width   

    def getArea(self):
        area = self.__length * self.__width
        return f"Area = {area}"

    def getPerimeter(self):
        perimeter = 2 * (self.__length + self.__width)
        return f"Perimeter = {perimeter}"
    
    def isSquare(self):
        if self.__length == self.__width:
             return True
        else:
             return False
        
myRectangle = Rectangle(10, 2)

print(myRectangle.getArea())
myRectangle.getPerimeter()
print(myRectangle.isSquare())
            

""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""

#Code 2

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.brand} {self.model} {self.year}"


class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year) 
        #ใช้superเพื่อจะเรียก constructor ของ Vehicle ให้อัตโนมัติ(เเนะนำให้ใช้เเทน)
        self.number_of_doors = number_of_doors

    def get_info(self):
        return f"{self.brand} {self.model} {self.year}, {self.number_of_doors}"

vehicle1 = Vehicle("Toyota", "cyberpunk1", 2077)
car1 = Car("Honda", "cyberpunk2", 2077, 4)

print(vehicle1.get_info())  
print(car1.get_info())


"""
Demonstrate polymorphism by creating:

    A base class Animal with method move()
    Three derived classes: Fish, Bird, Dog with different implementations of move()
        fish swims, bird flies, dog runs
    A function that takes any animal and calls its move() method
"""

#Code 3

class Animal:
    def __init__(self,name):
        self.name = name
    def move(self):
        print(f"{self.name}is move.")
class fish(Animal):  
    def __init__(self,name):
            super().__init__(name)
    def move(self):
            print(f"{self.name}swims")
class bird(Animal):  
    def __init__(self,name):
            super().__init__(name)
    def move(self):
            print(f"{self.name}fly")
class dog(Animal):  
    def __init__(self,name):
            super().__init__(name)
    def move(self):
            print(f"{self.name}runs")
            
def animal_move(animal):
    animal.move()

fishfriend = fish("fishfriend")
birdfriend = bird("birdfriend")
dogfriend = dog("dogfriend")

animal_move(fishfriend)    
animal_move(birdfriend)   
animal_move(dogfriend)