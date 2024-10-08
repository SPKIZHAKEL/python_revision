# an exception is an event that disrupts the flopw of the program
# eg ZeroDivisonError, TypeError, ValueError
# 1. try, 2.except and 3. finally
'''
try:
 # Try some code
except Exception:
 # handle an exception
finally:
 # Do some clean up
'''
try:
    number=int(input("Enter a number:"))
    print(1/number)

except ZeroDivisionError:
    print("You cant divide by 0")

except ValueError:
    print("enter only numbers please")

except Exception: #any other exception that is caught
    print("Something went wrong")

finally: # this block is for any additional checks (which will execute regardless of exception) like during file handling to make sure the file has been closed
    pass