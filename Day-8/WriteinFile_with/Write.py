file = open(r"C:\Users\ayush\OneDrive\Desktop\Python\Day-8\WriteinFile\data.text", "r")
data = file.read()
print("Before Change in file: ",data)
file.close()

file = open(r"C:\Users\ayush\OneDrive\Desktop\Python\Day-8\WriteinFile\data.text", "w")
file.write("Currenty i am stay in Hostel, 5678")
file.close()

file = open(r"C:\Users\ayush\OneDrive\Desktop\Python\Day-8\WriteinFile\data.text", "r")
data = file.read()
print("After Change in file: ",data)
file.close()