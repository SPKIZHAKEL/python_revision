# @property = Decorator used to define a method as property (it is defined as an attribute)
# benefit: Add additonal logic when read, write or delete attributes
# gives u a getter, setter and deleter object

class Rectangle:
    def __init__(self,width,height):
        self._height=height  # _ before the variable means this var is private and should not be accessed outside the class
        self._width=width    #to access the varibales u need to use a getter method

    @property
    def width(self): #thats a getter method
        return f"{self._width:.1f} cm"

    @property
    def height(self): #thats a getter method
        return f"{self._height:.1f} cm"
    @width.setter
    def width(self,new_width): #thats a setter method
        if new_width>0:
            self._width=new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self,new_height):
        if new_height>0:
            self._height=new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle=Rectangle(3,4)
print(rectangle.width)
print(rectangle.height) #so here since we added an additonal logic we could modify it

print(rectangle._width) #when i access the private varibales directly
print(rectangle._height)

#now if i try to set width of rectangle object to 0 it will show the setter output as should be greater than 0
#the getter output will show the original unchanged length,     
rectangle.width=0
rectangle.height=-1
print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height