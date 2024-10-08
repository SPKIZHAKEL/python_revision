#Inheritance = Allows a class to inherit attributes and methods from another class thereby promotinh reusability
#class Child(Parent) - so i dont need to rewrite it every time

class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal): #inheriting from animal class
    def speak(self):
        print(f"{self.name} is Woofing")

class Cat(Animal):
    pass

dog=Dog("socbby")
cat=Cat("luke")

print(f"{cat.name}")
print(f"{dog.is_alive}")

cat.eat()
dog.speak()
