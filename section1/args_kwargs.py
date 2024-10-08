# *args = allows u to pass multiple non-key args. we pack those args into a tuple
# **kwargs = allows u to pass multiple keyword aguments. we pack those args into a dictioanry

#  * - unpacking operator

#normally the below scenarion wont work

# def test(a,b):
#     return a+b
# test(1,2,3)

#however the *args keyword can be used to return a tuple. note u can use any other name like *num as well

def test(*args):
    print(type(args))
    for arg in args:
        print(arg)

test(1,2,3)

#in case of kwargs u can iterate over the keys or values or both since it packs the values into dictionary

def print_address(**kwargs):
    print(type(kwargs))
    for kwarg in kwargs.values():
        print(kwarg)
    print("**************************")
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_address(street="dholepatil road",
              city="Pune",
              state="maha",
              zip="41111"
              )

#u can use both *args and **kwargs together
print("#####################")
def test(*args,**kwargs):
    for arg in args:
        print(arg)
    print(f"{kwargs.get('sec')}") #use single quotes within double quotes else python will get confused where it ends
    for value in kwargs.values():
        print(value)


test("this","is","lol",first_name="im",last_name="testing",sec="both args and kwargs")


