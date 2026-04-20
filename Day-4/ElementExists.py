value = []

n = int(input("How many Number Do You want in your list: "))

for i in range(n):
    a = int(input(f"Enter {i+1} Number: "))
    value.append(a)

print(f"List = {value}")
find = int(input("Which Number Do You want to find: "))
found = False
for i in range(len(value)):
    if value[i] == find:
        print(f"Number is available at index {i}")
        found = True  
if not found:
    print("Number Not Available")