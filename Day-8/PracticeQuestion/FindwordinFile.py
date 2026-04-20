def find_word():
    word = "learning"
    with open(r"C:\Users\ayush\OneDrive\Desktop\Python\Day-8\PracticeQuestion\Practice.txt", "r") as file:
        data = file.read()
    if (word in data):
        print("Yes")
    else:
        print("No")
    file.close()

find_word()