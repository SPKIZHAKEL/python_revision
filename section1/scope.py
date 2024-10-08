#scope resolution= Local-> enclosed-> global -> built in (LEGB) (so it first checks locally then enclosed then global)


def func1():
    x=1

    def func2():
        x=2 #if i comment this then x=1 is chosen
        print(x)
    func2()

func1()


# now consider if there is no local version 

def test():
    print(y)

def test1():
    print(y)

y=1
test()
test1()

#now if i import a value using a built in, it has lower precedence than global since LEGB

from math import e

def test2():
    print(e)

e=4
test2()