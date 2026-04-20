print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

tip = int(input("How much do you Like gave? 10, 12, or 15? "))

split = float(input("How many People to split the bill? "))

total = (bill + (bill * (tip/100)) )/split

print(f"Each person should pay: ${round(total, 3)}")