print("PKR to USDT type :pkr \nUSDT into PKR type :dollar")
print("Q for Quit")

def currency_converterdollars(money):
    usdt=money/280
    return usdt

def currency_converterpkr(money):
    pkr=money*280
    return pkr

while True:
    user_input=input("enter the currency name or (q for quit):").lower()
    if user_input=="q":
        print("Good bye")
        break
    else:
        if user_input=="pkr":
            total=currency_converterpkr(float(input("enter the $ ammount to convert into pkr:")))
            print(f"total pkr is :{total:.2f}PKR")
            
        elif user_input=="dollar":
            
            total=currency_converterdollars(float(input("enter the pkr ammount to convert into $:")))
            print(f"total usdt is :{total:.2f}$")
        else:
            
            print("not valid currency")
 
    
    
