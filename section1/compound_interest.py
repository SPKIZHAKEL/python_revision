principal=float(input("Please enter the principal:"))
rate=float(input("Please enter the interest rate:"))
n=float(input("Enter the number of years:"))
t=float(input("number of time periods elapsed"))
amount=round(principal*pow((1+(rate/n)),t))

print(f"The amount is:{amount:.2f}")


