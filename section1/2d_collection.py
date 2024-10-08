#list of list
fruits=["apple","orange","banana","coconut"]
vegetables=["celery","carrots","potatoes"]
meats=["chicken","fish","turkey"]

groceries=[fruits,vegetables,meats]
print(groceries)

print(groceries[0])

for outer_row in groceries:
    for inner_row in outer_row:
        print(inner_row)
    print("\n")


#2 d tuple

num_pad=((1,2,3),
         (4,5,6),
         (7,8,9),
         ("*",0,"#"))
print(num_pad)