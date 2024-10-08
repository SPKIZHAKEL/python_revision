# class methods: allow operations on the class itself and instead of the instance i.e self u pass the
# class itself using cls parameter
import math
class Student:
    count=0
    total_gpa=0

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
        Student.total_gpa+=float(gpa)

    #instance method
    def get_info(self):
        return f"{self.name}{self.gpa}"

    @classmethod
    def get_count(cls): #passing the class as parameter and using the class variable
        return f"Total # of students:{cls.count}"
    
    @classmethod
    def get_average(cls):
        avg_gpa=(cls.total_gpa/cls.count)
        return f"Average gpa is {avg_gpa:.2f}"


  
#invoke class method

print(Student.get_count())

student1=Student("dummy","4.3")

print(student1.get_count())

student2=Student("dummy1","4.2")
print(student2.get_count())

student3=Student("Joe","3.4")

print(Student.total_gpa)

print(Student.get_average())