file = open(r"C:\Users\ayush\OneDrive\Desktop\Python\Day-8\Demo.txt", "w+")

print(file.read())
file.write("Demo Means Trial File")
print(file.read())
file.close()