#membership operator = used to test 
# whether a value or variable is found in a sequence (string, list, tuple, set or dictionary)
#in and not in

word="ORANGE"

letter=input("Guess a letter in the word")

if letter in word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")