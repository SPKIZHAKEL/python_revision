#object= A bundle of related attributes of variables and methods (a method is a function that belongs in an object)
# eg consider a cup it can have a liquid="coffee"
#
# u need a class to create many objects
#class= blueprint or layout of the object

class Car: #note its better to put the class in a sperate file eg if u put this class in car.py then u will import by from car import Car
    def __init__(self,model,year,color,for_sale):  #when creating a class u need to specify a constructor. self parameter points to this object we are creaing now
        self.model=model  #on the rhs are the parameters we receive
        self.year=year
        self.color=color
        self.for_sale=for_sale
    def drive(self):
        print(f"You drive the car {self.model}")
    def stop(self):
        print(f"You stop the car {self.model}")

car1=Car("BMW",2024,"red",False) #self is passed automcatically
car2=Car("Mustang",2023,"yellow",True)
print(car1) #will point to the car object in memory

print(car1.year)
print(car1.color)

car1.drive()
car2.drive()