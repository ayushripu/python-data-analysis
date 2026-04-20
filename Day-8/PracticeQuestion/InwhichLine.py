def in_Which_line():
    data = True
    word = "learning"
    line  = 1
    with open(r"C:\Users\ayush\OneDrive\Desktop\Python\Day-8\PracticeQuestion\Practice.txt", "r") as file:
        while data:
            data = file.readline()
            if (word in data):
                print(line)
                return
            line += 1
    return -1

in_Which_line()