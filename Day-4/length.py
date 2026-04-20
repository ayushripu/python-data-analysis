num = []

n = int(input("How Many Number Do You Want: "))

for i in range(n):
    a = int(input(f"Input {i+1} Number: "))
    num.append(a)

print(num)
 
print(f"Length Of The List is: {len(num)}") 