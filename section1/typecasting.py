'''typecasting: the process of converting a variable from one data type to another
str()
int()
float()
bool()

'''

name= "Dude"
age=2.5
gpa=(int(age))
print(type(name))
print(gpa)

age=str(age)

age+="1"
print(age)

#typecasting a sting to boolean will always give True unless empty

name=bool(name)
print(name)

name=""
name=bool(name)
print(name)