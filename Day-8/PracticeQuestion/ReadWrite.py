file = open(r"C:\Users\ayush\OneDrive\Desktop\Python\Day-8\Demo.txt", "r+")

data = file.write("ayush")

print(file.read())
file.close()