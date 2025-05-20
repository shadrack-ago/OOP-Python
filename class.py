# Defining a class
class car:
    color = "red" #attribute
    # Method
    def drive(self):
        print("The car is driving")

# Creating an object
my_car = car()
print(my_car.color)
my_car.drive()        

class Car:
    def __init__(self, color, model):
        self.color = color    # Instance variable
        self.model = model    # Instance variable

# Creating objects with unique attributes
car1 = Car("blue", "Sedan")
car2 = Car("red", "SUV")

print(car1.color)  # Output: blue
print(car2.model)  # Output: SUV

# implimented using functions
def car(color, model):
    return {
        "color": color,
        "model": model
    }
my_car = car("red", "sedan")
print(my_car["color"])  # Output: red
print(my_car["model"])  # Output: sedan