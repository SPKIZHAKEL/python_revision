#concise way to create lists in Python, which are more compact than traditional loops
# ["expression" for "value" in iterable if condition]

doubles=[]
for x in range(1,11):
    doubles.append(x*2)

print(doubles)

doubles=[x*2 for x in range(1,5)]
print(doubles)

triples=[y*3 for y in range(1,5)]
print(triples)

fruits=["apple","bananna","pineapple","ginger"]
fruits=[fruit.capitalize() for fruit in fruits]
print(fruits)

numbers=[1,-2,3,-4,5,-6]
numbers=[abs(number) for number in numbers]
print(numbers)