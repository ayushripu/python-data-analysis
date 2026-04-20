Value = []

n = int(input("How many Number Do You want in a list: "))

for i in range(n):
    a = int(input(f"Enter {i+1} Number: "))
    Value.append(a)
print(f"list = {Value}")

find = int(input("Which value do you want to check: "))
count = 0
found  = False
for i in range(len(Value)-1):
    if find  == Value[i]:
        count += 1
        
print(f"{find} appears in List is {count} Times")