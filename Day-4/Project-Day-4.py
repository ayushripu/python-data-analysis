import random
game = ["Rock", "paper", "Scissors"]

Choose = (int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. : ")))

choice = random.choice(game)
if Choose >= 3 or Choose < 0:
    print("Wrong Input")
elif game[Choose] > choice:
    print(f"Computer choice: {choice}")
    print(f"You Choose {game[Choose]}")
    print("You win!")
elif game[Choose] < choice:
    print(f"Computer choice: {choice}")
    print(f"You Choose {game[Choose]}")
    print("You lose")
elif game[Choose] == choice:
    print(f"Computer choice: {choice}")
    print(f"You Choose {game[Choose]}")
    print("It's a draw")

