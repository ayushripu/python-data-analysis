n = set()

n.add(8)
n.add("Ayush")
n.add(85.90)
n.add(4)
n.add((8, 9, 36, 7))
 
print("Direct Set Value Before Removing: ",n)
n.remove("Ayush")
print("Direct Set Value After Remove: ",n)

#####################################################################

empty = set()

number = int(input("How many number do you want in your set: "))

for i in range(number):
    num = input(f"Enter {i+1} Number: ")
    empty.add(num)


print("Set Value through User Input Before Remove: ",empty)

rem= input("Which Value You want to Remove: ")
empty.remove(rem)

print("Set Value through User Input After Remove: ",empty)