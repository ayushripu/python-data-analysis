l1 = []
num = int(input("How many Number Do You Want in your list: "))

i=0
total = 0
while i < num:
    newNum = int(input(f"Input {i+1} Number: "))
    l1.append(newNum)

    total += newNum
    i+=1

print(f"List = {l1}")
print(f"Sum of Total number in Your list is : {total}")
