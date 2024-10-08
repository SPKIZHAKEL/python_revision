# resuable piece of code

def happy_birthday():
    print("Happy birthday")

happy_birthday()


def happy_birthday(name,age):
    print(f"Happy Birthday {name} {age}")

happy_birthday("Bro",20)

#return is a statement used to end a fucntion and send result back ti caller

def add(x,y):
    z=x+y
    return z

print(add(1,2))