l1 = []
num = int(input("Input How many Number In Your list: "))

i =0
fac =1

while i < num:
    newNum = int(input(f"Enter {i+1} Number "))
    l1.append(newNum)
    fac *= newNum
    i+=1

print(f"List = {l1}")
print(f"Factorial Of list: {fac}")