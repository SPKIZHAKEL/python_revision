temp=input("Enter C or F:")
temp_val=float(input("Enter the actual temperature"))

if temp=="C":
    temp_far=(temp_val*(9/5))+32
    print(f"temp in fahrenheit is {temp_far}")
elif temp=="F":
    temp_cel=(temp_val-32)*(5/9)
    print(f"temp in celsius is {temp_cel}")
else:
    print("Enter a valid temp")