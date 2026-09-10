print("Welcome to Piza Delevery")
size=input("What size you want? S M or L :")
peperoni=input("Do you want Peperoni on Pizz  Y/N : ")
extra_chese=input("Do you need extra Cheese  Y/N : ")

pizza_total_price=0
if size=='s':
    pizza_total_price=10
elif size=='m':
    pizza_total_price=15
elif size=='l':
    pizza_total_price=20
else:
    print("Please Enter valid choices")

if peperoni=='y':
    if size=='s':
        pizza_total_price+=2
    elif( size=='m'or size=='l'):
        pizza_total_price+=3
if extra_chese=='y':
    pizza_total_price+=2
print("Your total bill is :",pizza_total_price  )