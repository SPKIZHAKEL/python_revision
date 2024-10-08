#Iterable = An object/collection that can return its elements one at a time, allowing it to be iterated over a loop
#like list, tuples, set
#note u cant reverse a set since its unordered!!!
numbers=[1,2,3,4,5]

for number in numbers:
    print(number)

fruits={"apple","banana","cocunut"}
fruits1={"A":1,"B":2,"C":3}

for fruit in fruits:
    print(fruit)

    #by default keys are printed from the dictionary only for values and items u need to specify

    for key in fruits1:
        print(key)

    for key,value in fruits1.items():
        print(f"{key}:{value}")