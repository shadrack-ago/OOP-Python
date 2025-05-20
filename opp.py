# OOP Principles: Inheritance, Polymorphism, and Encapsulation
# Inheritance,
class car:
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive(self):
        print(f"The {self.color} {self.model} is driving")  
class ElectricCar(car):
    pass
class HybridCar(car):
    pass

ElectricCar=car("blue", "Tesla")
HybridCar=car("red", "Toyota")
print(ElectricCar.color)  # Output: blue
print(HybridCar.model)  # Output: Toyota
ElectricCar.drive()  # Output: The blue Tesla is driving
HybridCar.drive()  # Output: The red Toyota is driving

# Polymorphism 🦄
class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Woof!" 
class Cat(Animal):
    def sound(self):
        return "Meow!"
class Cow(Animal):
    def sound(self):
        return "Moo!"
# Creating a list of animals
animals = [Dog(), Cat(), Cow()]
# Looping through the list and calling the sound method
for animal in animals:
    print(animal.sound())  # Output: Woof! Meow! Moo!    

# Encapsulation 🔐: 
# Restricting access to certain components of an object
class SecretStash:
    def __init__(self):
        self.__chocolates = 10  # Private attribute

    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("One chocolate taken!")
        else:
            print("No chocolates left")

stash = SecretStash()
stash.take_chocolate()