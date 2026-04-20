marks ={}

for i in range(3):
    sub =input(f"Enter {i+1} Subject Name: ")
    score= int(input(f"Enter the marks of {sub}: "))
    marks[sub] = score

print(marks)
