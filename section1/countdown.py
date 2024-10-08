import time

my_time=int(input("Enter the number of seconds to sleep:"))

minutes=round(my_time/60)
#if u wanted to make sure that this value doesnt go abv 60 use (my_time/60)%60
hours=minutes%60
for x in range(0,my_time):
    print(f"{hours:02}:{minutes:02}:{x:02}")
    time.sleep(1)

print("times up")

#for incrementing backwards

for x in range(my_time,0,-1):
    print(x)
    time.sleep(1)

print("TIMES UP") 