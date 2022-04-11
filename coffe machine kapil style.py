menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print("sorry there is not enough ingredients to make a coffe")
            return False
    return True

def process_coins():
    print("Please insert coins")
    quarters=int(input("please enter quarters : ")) * 0.25
    dimes=int(input("please enter dimes : ")) * 0.1
    nickels=int(input("please enter nickels : ")) * 0.05
    pennies=int(input("please enter pennies : ")) * 0.01
    total=quarters+dimes+nickels+pennies
    print(round(total,2))
    return total

def is_transaction_successful(moneyreceived,drinkcost):
    if moneyreceived >= drinkcost:
        change=round(moneyreceived-drinkcost,2)
        print(f"your change is {change}")
        global profit
        profit+=drinkcost
        return True
    else:
        print(" sorry you dont have enough money to buy the coffee the money is refunded")
        return False

def make_cofee(drinkname,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
        print(f"here is your coffee {drinkname}, Enjoy !")
        


on =True
while on:
 choice=input("which kind of coffee would you like to have (espresso/latte/cappuccino):  ")
 if choice=="off":
     on = False
     print(" you turned off coffee machine")
 elif choice=="report":
     print(f"water : {resources['water']} ml")
     print(f"milk : {resources['milk']} ml")
     print(f"coffee : {resources['coffee']} gm")
     print(f"money : {profit} $")
 else:
     drink=menu[choice]
     if is_resources_sufficient(drink["ingredients"]):
         payment=process_coins()
         if is_transaction_successful(payment, drink["cost"]):
             make_cofee(choice, drink["ingredients"])
             
