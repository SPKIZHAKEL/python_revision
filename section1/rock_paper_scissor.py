import random
options=["rock","paper","Scissor"]
my_score=0
bot_score=0
res1="t"
while res1=="t":
    print("Choose one of the 3:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    res=int(input("Enter ur choice:"))
    option=random.choice(options)
    print(option)
    if int(res)==(options.index(option)+1):
        print("Draw")
        break
    elif res==1:
        if option=="Paper":
            bot_score=bot_score+1
        elif option=="Scissor":
            my_score=my_score+1
            print(my_score)
    elif res==2:
        if option=="Rock":
            my_score=my_score+1
        elif option=="Scissor":
            bot_score=bot_score+1
    elif res==3:
        if option=="Rock":
            bot_score=bot_score+1
        elif option=="Paper":
            my_score=my_score+1
    print(my_score)
    print(bot_score)
    max_val="u won" if my_score > bot_score else "bot won"
    print(f"winner is:{max_val}")
    print("----------------")
    res1=input(("do u want to continue? t/f"))