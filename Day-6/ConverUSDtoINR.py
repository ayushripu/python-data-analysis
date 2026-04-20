usd = int(input("Enter Dollar Amount : " ))
rup = 83
def CurrencyConverter(money):
    inr = usd*rup
    print(f"{usd}$ = {inr}Rup")
    return inr

CurrencyConverter(usd) 