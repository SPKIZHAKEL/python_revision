#the __name__== '__main__' is used to check if the current code is being run directly i.e if when we run
#then in the config is it set to main_demo in this case. in the code below we are running main_demo.py directly hence its __name__==__main__
#but the main_not.py since we import it indirectly its __name__ will be main_demo
#basically unless its the main module u dont want to execute main function so we use the if condition for the same to check if current module is main module
#alt u want to use just one function from another script but not import the main module
'''
Since there is no main() function in Python, when the command to run a python program is given to the interpreter, the code that is at level 0 indentation is to be executed. However, before doing that, it will define a few special variables. __name__ is one such special variable. If the source file is executed as the main program, the interpreter sets the __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module’s name.
__name__ is a built-in variable which evaluates to the name of the current module. Thus it can be used to check whether the current script is being run on its own or being imported somewhere else by combining it with if statement

'''
from main_not import *

def demo():
    print("this is a test")
def main():
    print(__name__)
    demo()
if __name__=="__main__":
    main()
