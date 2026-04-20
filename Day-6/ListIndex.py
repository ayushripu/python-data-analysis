def l1_indx(list, index):
    if index == len(list):
        return 0
    else:
        print(list[index])
        l1_indx(list, index+1)

city = ["Patna", "Delhi", "Mumbai", "Goa"]

l1_indx(city, 0)