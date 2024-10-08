import random

num=random.randint(1,6)

print(num)

#for a random floating point number
res=random.random()
print(res)

#also if u want to generate a random one out of given options we use choice

options=["a","b","c"]
print(random.choice(options))

#also u can shuffle cards
cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)