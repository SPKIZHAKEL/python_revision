foods=[]
prices=[]
total=0


while True:
    res=input("Would u like to continue:y/n ")
    if res.lower()=="y":
        price=int(input("enter the price:"))
        food=input("enter the food:")
        prices.append(price)
        foods.append(food)
    elif res.lower()=="n":
        break

for i in range(len(prices)):
    print(i)
    total+=prices[i]
print(f"your total bill is {total}")
for i in range(len(foods)):
    print(f"The item {i+1} is {foods[i]}")

