'''
multiple inheritance = inherit from one or more parent class eg C(A,B)

multilevel inheritance = u inherit from one parent which inherits from another parent
eg C(B)<-B(A)<-A

'''
class Animal:
    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} this animal is eating")
class Prey(Animal):
    def flee(self):
        print(f"This {self.name} animal is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"This {self.name} animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): #fish is both prey and pred so lets use multiple inheritance
    pass

rabbit=Rabbit("Roger")
fish=Fish("gagan")

rabbit.flee()

fish.hunt()
rabbit.eat()
fish.eat()