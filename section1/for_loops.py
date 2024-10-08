#better than while when u need to do things a fixed number of times, u can iterate over a range, string or anything that is iterable
#range has exclusive upper limit i.e (1,11) will print 1 to 10

for i in range(1,11):
    print(i)


#to print in reverse use the reversed function

for x in reversed(range(1,11)):
    print(x)

# to use step

for i in range(1,10,3):
    print(i)

#continue keyword: is used to skip a particular iteration

for i in range(1,21):
    if i==13:
        continue
    else:
        print(i)

#if u want to break the loop use break keyword

print("########",end="\n")
for i in range(1,21):
    if i==13:
        break
    else:
        print(i)