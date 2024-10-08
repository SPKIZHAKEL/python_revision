#dictionary = collection of {key:value} pairs ordered and changeable. no duplicates

capitals={"USA":"DC",
          "India":"Delhi",
          "China":"Beijing",
          "Russia":"Moscow"}

print(capitals.get("China")) #will return the associated value

capitals.update({"Germany":"Berlin"})
print(capitals)

capitals.update({"USA":"DETROIT"})
print(capitals)

capitals.pop("China")
print(capitals)

capitals.popitem() #last item
print(capitals)

keys=capitals.keys()

print(keys)

values=capitals.values()

print(values)

items=capitals.items() #converts into a 2d tuple
print(items)

for key,value in items:
    print(f"{key}:{value}")