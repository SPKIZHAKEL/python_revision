#keyowrd arg an arg preceded by an identifier which helps with readability, order of args doesnt matter since the function 
#takes them based on identifier
#but if u are mixing other types of args then make sure keyword args come after positional args else u will get an error


def hello(greeting,title,first_name,last_name):
    print(f"{greeting} {title} {first_name} {last_name}")

hello("Good Morning",last_name="singh",first_name="vaibhav",title="Maharaj")

#even print function uses keyword args

print("1","2","3","4","5",sep="-")