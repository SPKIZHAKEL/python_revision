# [start: end: step] note the end index is exclusive i.e its actually n-1

credit_number="1234-5678-9012-3456"

print(credit_number[4])

print(credit_number[0:4]) # 0 to 4-1=3

print(credit_number[5:])#last 12 digits

print(credit_number[-1])

#printing every 2nd char in a string starting from the 1st

print(credit_number[::2])

# u can also index from the back eg to only have last 4 digits visible

print(f"XXXX-XXXX-XXXX-{credit_number[-4:]}")

#reverse the chars in string
credit_number="1234-5678-9012-3456"
print(credit_number[-1:-21:-1])

#or better way to reverse

print(credit_number[::-1])