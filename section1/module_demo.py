'''
module= a file containing code u want to include in ur program which  can be a built in code or ur own
u can break up learge files into smaller reusable files

'''

#when ur using the imported value and it overlaps with an exisitng variable make sure that u precede it with module_name
import math
import example


a=5
print(math.e ** a)


print(example.circumference(a))
print(example.cube(2))