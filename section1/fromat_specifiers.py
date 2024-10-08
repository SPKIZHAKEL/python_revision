'''
format a value based on flags inserted
format specifiers={value:flags}


:(number) = allocate that many spaces
:.(number)f =round to that many decimal places
:03 = allocate and zero pad that many spaces
:< = left justify
:> = right justify
:^ = centre align
:+ = plus sign to indicate postive value
:= = place sign to the leftmost position
:  = insert space before psootive numbers
:, = comma separator
'''

price1=3.14159
price2=-987.65
price3=12.34
price4=10000
print(f"Price is {price1:.2f}")
print(f"Price is {price2:>10}") # right jsutified in 10 spaces including the number itself
print(f"Price is {price3:10}") # so in total inclduign the number itslef there are 10 spaces to preceed it with zero {price3:010}
print(f"Price is {price3:+}")
print(f"Price is {price4:,}") #to seperate based on decimal
print(f"Price is {price4:+,.2f}") # u can combine flags as well