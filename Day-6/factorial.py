fact = int(input("Which Number You Wnat To Factorial: "))

def factorail(n):
    i =1
    f =1
    while i <= fact:
        f *= i
        i+=1
    print(f"Factorail of {fact } is:",f)

factorail(fact)