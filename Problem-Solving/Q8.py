# Create a list of 10 numbers 
# and print the largest and smallest number.


li = []
for i in range(10):
    s = int(input(f"{i+1} : "))
    li.append(s)

print("List  = ",li)
print("Max Value = ", max(li))
print("Min Value = ", min(li))