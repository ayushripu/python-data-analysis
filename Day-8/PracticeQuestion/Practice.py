with open(r"C:\Users\ayush\OneDrive\Desktop\Python\Day-8\PracticeQuestion\Practice.txt", "w") as file:
    file.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java")
file.close

with open(r"C:\Users\ayush\OneDrive\Desktop\Python\Day-8\PracticeQuestion\Practice.txt","r") as file:
    data = file.read()

new_data = data.replace("Java", "Python")
print(new_data)

with open(r"C:\Users\ayush\OneDrive\Desktop\Python\Day-8\PracticeQuestion\Practice.txt", "w") as file:
    file.write(new_data)
file.close