age=int(input("Enter your age"))

# if age>=18:
#     print("you are signed up")
# else:
#     print("u must be 18+")

if age>=18:
    print("u are an adult")
elif age<0:
    print("enter an invalid age")
else:
    print("u must be an adult to sign up")