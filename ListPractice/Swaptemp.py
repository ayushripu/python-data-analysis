l1 = ["Apple", "Banana", "Papaya", "Watermelon", "Orange"]
print(l1)

temp  = l1[0]
l1[0] = l1[2]
l1[2] = temp

print(l1)