value = []

a = int(input("How Many Numner Do You want: "))

for i in range(a):
    n = int(input(f"Enter {i+1} Number: "))
    value.append(n)
    if a == len(value):
        last = value[i]

print(f"List = {value}")
print(f"Last Value Of Lis is: {last}")