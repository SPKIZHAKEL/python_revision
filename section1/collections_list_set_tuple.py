'''
collection is like a singel varibale to store multiple calues
List = [] ordered and changeabl. Duplicates are ok
Set = {} unordered and immutable, but Add/Remove ok. NO duplicates
Tuple = () ordered and unchaeabl. Duplicates ok. Faster
'''

fruits=["apple","orange","banana","cococnut"]
print(fruits)
print(fruits[::1])

for fruit in fruits:
    print(fruit)

    #dir command is used to look at all attributes of an object
print(dir(fruits))

print(len(fruits))

#to check if an item is present in the list

print("apple" in fruits)

#u can change the item by just reassigning the value

fruits[0]="pineapple"

print(fruits[::1])

#reverse
print(fruits[::-1])

#add
fruits.append("chocolate")

#remove

fruits.remove("banana")

#insert at index

fruits.insert(0, "dragon fruit")

#sort in alphabetical order
fruits.sort()
print(fruits)

#reverse
fruits.reverse()
print(fruits)

#to find index
print(fruits.index("orange"))
print(fruit.count("orange"))
#to clear list

fruits.clear()
print(fruits)


#------SET-------
#almost same as list but index wont work!! since set is unordered. 
fruits1={"apple","orange","banana","coconut"}

#pop removes first element but its random
print(fruits1)
fruits1.pop()
print(fruits1)

#no duplicates are allowed
fruits1.add("coconut")
print(fruits1)

#------tuple--------

fruits3=("apple","banana","orange","coconut")
print(fruits3)
fruits3.count("coconut")
print(fruits3.index("orange"))