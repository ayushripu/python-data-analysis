print("Welcome to Teasure Island. \nYour Mission is to find th e treasure.")
print("You're at a cross road. Where do you want to go? ")
choise1 = input("Type left or right: ").lower()
if choise1 == "left":
    choise2 = input('You\'ve come to a lake.'
                    'There is an island in the middle of the lake.'
                    'Type "wait" to wait for a boat.' 
                    'Type "swim" to swim across.').lower()
    if choise2 == "wait":
        choice3 = input('You arrive at the island unharmed.'
                        'There is a house with 3 doors.'
                        'One red, one yellow and one blue.'
                        'Which colour do you choose?').lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice3 == "blue":
            print("blue You enter a room of beasts. Game Over.")
        else:
            print("You Choose a door does't Exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")