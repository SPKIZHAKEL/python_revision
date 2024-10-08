'''
a decorator is a function which extends the behaviour of another function 
w/o modifying the base function

Pass the base function as an argument to the decorator

eg below base function 
get_ice_cream("vanilla") here we wanna create a decorator for adding sprinkes without modifying the functions

@add_sprinkles
get_ice_cream("vanilla")

'''
def add_sprinkles(func):
    def wrapper(*args,**kwargs): # the wrapper is needed because if it wasnt there the decorator will execute and the base funciton will execute even when base funciton is not called
                # to make sure that the decorator is ONLY called when the base function is executed (called) in the code       
        print("You add sprinkles")
        func(*args,**kwargs)
    return wrapper

def add_fudge(func): 
    def wrapper(*args,**kwargs):
        print("You add fudge")
        func(*args,**kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"{flavour} Here is ur ice cream")  #now if i put a value here and dont put args and kwargs in decorator i would get error

get_ice_cream("vanilla")