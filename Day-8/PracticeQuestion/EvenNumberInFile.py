with open(r"C:\Users\ayush\OneDrive\Desktop\Python\Day-8\PracticeQuestion\Number.txt", "r") as file:
    data = file.read()
    print (data)

count = 0
nums = data.split(",")
for val in nums:
    if int(val) % 2  == 0:
        count += 1
        
print("Total Even Number is :",count)

    