print("welcome to  the pizza deliveries! ")
bill = 0
size = input("What the pizza size do you want? S, M, L: ")
pepporoni = input("Do you want pepporoni on your pizz? Y or N: ")
extra_cheese = input("Do you want Extra cheese Y or N: ")

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("You Type the Wrong Input.")

if pepporoni == "Y":
    if size == "S":
        bill +=2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")