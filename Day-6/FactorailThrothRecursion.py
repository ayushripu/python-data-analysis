def factorial(Num):
    if Num == 0 or Num == 1:
        return 1
    else:
       return factorial(Num-1) * Num
   

print(factorial(4))