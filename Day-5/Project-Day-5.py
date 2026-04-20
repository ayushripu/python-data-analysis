import random

Letter =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number =['0','9','8','7','6','5','4','3','2','1']
symbol =['!','@','#','$','%','^','&','*','(',')','_','+']

print("Welcome to the PyPassword Generator!")

letter_range = (int(input("How many letters would you like in your password?\n")))
symbol_range = (int(input("How many Symbols Would You Like?\n" )))
number_range = (int(input("How many numbers would you like?\n")))

passw = []
for char in range(0, letter_range):
    passw.append (random.choice(Letter))

for char in range(0, symbol_range):
    passw.append(random.choice(symbol))

for char in range(0, number_range): 
    passw.append(random.choice(number))

random.shuffle(passw)
l = ""
for password in passw:
    l += password

print("Your password is: "+l)