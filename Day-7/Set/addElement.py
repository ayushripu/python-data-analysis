n = set()

n.add(8)
n.add("Ayush")
n.add(85.90)
n.add(4)

print("Direct Set Value: ",n)

################################################################

empty = set()

number = int(input("How many number do you want in your set: "))

for i in range(number):
    num = input(f"Enter {i+1} Number: ")
    empty.add(num)

print("Set Value through User Input: ",empty)