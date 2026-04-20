value = []
a = int(input("How many Number Do You want in List: "))
index = int(input("On Wich Index VAlue do You want "))

for i in range(a):
    num = int(input("input  Number: "))
    value.append(num)

NewValue = int(input("Which Nuumber Do You Want To add: "))
if index <= len(value):
    value.insert(index, NewValue)
else:
    print("Index Value Out Of Bound")

print(value)