#hangman game
import random
options=("apple","orange","pineapple","banana","dragon fruit")

hangman_art={
    0:(" ",
       " ",
       " "),
1:(" o ",
   "   ",
   "   "),
2:(" o ",
   " | ",
   "   "),
3:(" o",
   "/|",
   "   "),
4:(" o",
   "/|\\",
   " "),
5:(" o",
   "/|\\",
   "/  "),
6:(" o",
   "/|\\",
   "/ \\"),
}
#testing if the art is working
def hangman_art_print(count):
    for tuple_item in hangman_art[count]:
        print(tuple_item,sep="\n")



def match_case_for_wrong_guess(word_to_be_guessed,wrong_cnt):
    match wrong_cnt:
        case 1:
            hangman_art_print(wrong_cnt)
            return word_to_be_guessed,wrong_cnt
        case 2:
            hangman_art_print(wrong_cnt)
            return word_to_be_guessed,wrong_cnt
        case 3:
            hangman_art_print(wrong_cnt)
            return word_to_be_guessed,wrong_cnt
        case 4:
            hangman_art_print(wrong_cnt)
            return word_to_be_guessed,wrong_cnt
        case 5:
            hangman_art_print(wrong_cnt)
            return word_to_be_guessed,wrong_cnt
        case 6:
            hangman_art_print(wrong_cnt)
            print("You exhausted your options!, You lost")
            exit()
            return word_to_be_guessed,wrong_cnt
       

def print_pattern_for_iteration(word_to_be_guessed, word_to_be_guessed_1,guess,wrong_cnt):
    if guess in word_to_be_guessed_1:
        for i, letter in enumerate(word_to_be_guessed):
            if guess==str(letter):
                print(f" {guess} ",end="\t")
            elif letter=="#":
                # print(f"******{i}******",end="\n\n")
                print(f" {word_to_be_guessed_1[i]} ", end="\t")
            else:
                print(" _ ",end="\t")
        #removing the already guessed letter
        word_to_be_guessed=str(word_to_be_guessed).replace(guess,"#")
        #easier approach woudl be to just update the origial string at the index
        return word_to_be_guessed,wrong_cnt
    else:
        wrong_cnt=wrong_cnt+1
        res1=match_case_for_wrong_guess(word_to_be_guessed,wrong_cnt)
        return res1
    
#Main code
second_flag=False
first_flag=True

wrong_count=0
while (wrong_count<=6):
    if wrong_count==0 and first_flag:
        word_to_be_guessed=random.choice(options)
        word_to_be_guessed1=str(word_to_be_guessed)
        print(word_to_be_guessed)
        first_flag=False
    guess=input("Enter your guess:").lower()
    (res,wrong_count)=print_pattern_for_iteration(word_to_be_guessed,word_to_be_guessed1,guess,wrong_count)
    res2=str(res)
    print(res2)
    print(wrong_count)
    print("************")
    print(word_to_be_guessed)
    print(word_to_be_guessed1)
    
    count_2=0
    for letter in res2:
        if letter!="#":
            count_2+=1
    if count_2==0:
        print(f"YAYY U GUESSED THE WORD {word_to_be_guessed1}")
        exit()
    wrong_count=int(wrong_count)
    word_to_be_guessed=str(res)