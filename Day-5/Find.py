l1 = [8,6,9,1,2,7,9]
print(l1)

num   = int(input("So, tell me Which Number Do You Want To Search: "))

for i in range(len(l1)-1):
    if num == l1[i]:
        print("Found at index ",i)
   