
height = int(input("Enter Your Height: "))

if height >= 120:
    age = int(input("Input age: "))
    print("You can Ride the Rollercoaster")
    if age <= 18:
        if age <= 12:
            print("Please Pay 5$")
        else:
            print("Please Pay $7.")
    else:
            print("Please pay $12.")                
else:
    print("Sorry You have to grow taller before you can ride") 