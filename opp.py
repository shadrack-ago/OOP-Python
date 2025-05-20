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
