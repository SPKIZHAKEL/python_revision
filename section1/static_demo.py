# Static method: It is a method that belongs to a Class rather than an object from the class
# we use it in general utility functions

# Instance methods = best for operations on instances of the class (objects)
'''
eg:
def get_info(self):
    return f"{self.name}={self.position}"

'''
# Static methods = best for utility functions that do not need access to the class data

'''
@staticmethod
def km_to_miles(kilometers):
    return kilometers * 0.621371
'''


# difference between the 2

class Employee:

    def __init__(self,name,position):
        self.name=name
        self.position=position

    def get_info(self):
        return f"{self.name}={self.position}"

    @staticmethod
    def is_valid_pos(position):  #a static method doesnt have a self parameter since ur not working on the object created from the class
        valid_positions=["Manager","Cook","Cashier","Janitor"]
        return position in valid_positions # so now to use this method we dont need to instantiate the class
    
emp1=Employee("jake","Cook")
print(emp1.get_info()) #instance method
print(Employee.is_valid_pos("Cook"))#static method
print(Employee.is_valid_pos("haha"))