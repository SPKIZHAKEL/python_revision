'''
Duck typing: another way to achieve polymorphism besides Inheritance is duck typing
object must have the minimum necessary attributes/methods
"If it looks like a duck and quacks like a duck it must be a duck"
'''

class Animal:
    alive=True

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Car:
    alive=False
    def speak(self):
        print("HONK")

animals=[Dog(), Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

#although the Car object doesnt inherit from other classes since it has a method and attribute like Animal
#it can be considered one

