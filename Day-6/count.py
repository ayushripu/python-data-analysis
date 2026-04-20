def count(list, indx):
    if indx == len(list):
        
        return 0
    
    else:
       return 1 + count(list, indx+1)
        

n = ["Ayuhd", "Ljdkh", "hsufhu", "Ayush"]
c = count(n,0)

print("Count = ", c)



