'''
super() - function is used by a child class to call methods from the parent class, allows u to extend functionality of the inherited methods
'''

#in the below code we see that the attributes color and filled in the parent class are being 
#again defined in the child classes. Instead of defining it again we can use the super keyword to call the constructor from the parent class
# and then add the appropriate attributes as needed in our class
# class Shape:
#     def __init__(self,color,filled):    
#         self.color=color
#         self.filled=filled

# class Circle(Shape):
#     def __init__(self,color,filled,radius):
#         self.color=color
#         self.filled=filled
#         self.radius-=radius
# class Rectange(Shape):
#     def __init__(self,color,filled,height):
#         self.color=color
#         self.filled=filled
#         self.height=height
# class Square:
#     def __init__(self,color,filled,width):
#         self.color=color
#         self.filled=filled
#         self.width=width


#so the same code using super keyord!! we willbe calling the constructor from the parent
# just imagine that wherever super() is there we use the class
import math
class Shape:
    def __init__(self,color,filled):    
        self.color=color
        self.filled=filled
    def describe(self):
        print(f"it is {self.color} and {self.filled}")

class Circle(Shape):
    def __init__(self,color,filled,radius):
        super().__init__(color, filled)
        self.radius=radius
    #overriding the describe method
    def describe(self):
        print(f"the area of the circle is {math.pi*pow(self.radius,2)}")
        #also using the parent describe method
        super().describe()

class Rectange(Shape):
    def __init__(self,color,filled,height):
        super().__init__(color,filled)
        self.height=height
class Square(Shape):
    def __init__(self,color,filled,width):
        super().__init__(color,filled)
        self.width=width
    def describe(self):
    #overriding the describe method
        print(f"the area of the square is {pow(self.width,2)}")
        super().describe()

circle=Circle("red",True,6)
square=Square("blue",False,4)
print(circle.radius)

print(circle.describe()) #will take the child class implementation
print(square.describe()) #will take the parent class implementation