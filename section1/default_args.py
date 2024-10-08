#default args are a default value for a certain param, when certain params are omitted, it helps reduce number of args

def net_price(list_price,discount=0,tax=0.05):
    return list_price*(1-discount)*(1+tax)

print(net_price(500))

#when we pass an arg we use that instead of what is default

print(net_price(500,0.1))

# vimp default args can come only after positional args i.e def count(start=0, end)