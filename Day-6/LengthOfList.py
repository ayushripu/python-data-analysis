City = []
cn = int(input("How Many City You Want In Your List: "))

i =0
while i < cn:
    tcn = input(f"Input {i+1} City Name: ")
    City.append(tcn)
    i+=1
print("Your Total City is : ",City)

def length(List):
    print("Lenget of List is :",len(List))
    return len(List)

length(City)