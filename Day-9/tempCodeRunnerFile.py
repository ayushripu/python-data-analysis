[i for i in range(100000000)]
list2 = [i for i in range(100000000,200000000)]
list3 = []

for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
print(f"Ti