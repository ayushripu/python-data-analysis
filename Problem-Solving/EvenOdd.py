a = [5, 2, 4, 8, 6, 7, 3]
even = 0
odd = 0
for i in range(len(a)):
    if a[i]%2 == 0:
        even  = even+1
    else:
        odd = odd+1


print("Even : ",even)
print("Odd  : ",odd)