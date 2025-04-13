class Animal:
    def move(self): pass


class Car(Animal):
    def move(self):
        print("Driving")

class Bird(Animal):
    def move(self):
        print("Flying")


car = Car()
bird = Bird()


car.move()  # Outputs: Driving
bird.move()  # Outputs: Flying 

# For example, if we add a Bike class
class Bike(Animal):
    def move(self):
        print("Cycling")


bike = Bike()
bike.move() 