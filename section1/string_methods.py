#note by default print function prints on new line since the def of the function is print(objects,sep=seperator by default is '',end='\n')
#to print on same line print("Hello",end=" ")
'''
name="raja natwarlal"

print(len(name))

#to find first occuremce of a char
print(name.find("a"))

#to find the last occurecne
print(name.rfind("a"))

#to capitalize first letter
print(name.capitalize())

# all upper cause
name=name.upper()

#all lower
name=name.lower()

#if digit or not
print(name.isdigit())

#f ionly alphabets but if it contains space it will come false or any digits
print(name.isalpha())

#count number of chars in a string
print(name.count(" "))

#replace a char by another
print(name.replace(" ","-"))

#all methods of string docs
print(help(str))

'''

#validate user input

username=input("Please enter a username:")

if len(username)>12:
    print(f"too many chars {username}")
elif username.find(" "):
    print(f"space in username")
elif username.isdigit():
    print(f"should not contain digits {username}")
else:
    print(f"username is {username}")

