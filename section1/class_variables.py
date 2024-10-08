'''
class variables= Shared among all instances of a class unlike instance variables
defined outside the constructor
allow u to share data among objects created from that class
'''

class Student:

    class_year=2024 # this is the class variable shared by all of them
    num_students=0
    def __init__(self,name,age):
        self.name=name #instance vars
        self.age=age #instance vars
        Student.num_students+=1 #since below we have create 2 objects and this var is shared its gonna be val 2


student1=Student("Spongebob",30)
student2=Student("Patrick",20)

print(student1.age)
print(student2.age)
print(student1.class_year)
print(student2.class_year)
#its better to access class vars using the Class name rather than the instance

print(Student.class_year)
print(Student.num_students)