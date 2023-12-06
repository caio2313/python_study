# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
end_turn = False
MENU = {
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
coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}

def check(order):
    suficiente = True
    for item in MENU:
        items = MENU[item]
        ingredientes = items['ingredients']
        custo = items['cost']
        if order == item:
            # print(f"{item}: {ingredientes} {custo}")
            for ing in ingredientes:
                if ingredientes[ing] > resources[ing]:
                    faltando = ing
                    print(f"Sorry there is not enough {faltando}.")
                    suficiente = False
            if suficiente:
                paid = 0
                quart = int(input("How many quarters? "))
                paid += quart * coins['quarters']
                dec = int(input("How many dimes? "))
                paid += dec * coins['dimes']
                cinq = int(input("How many nickles? "))
                paid += cinq * coins['nickles']
                uno = int(input("How many pennies? "))
                paid += uno * coins['pennies']
                payment = round(paid, 2)
                print(f"payment: {payment}")
                if custo > payment:
                    print("Sorry, that's not enough money. Money refunded.")
                elif payment == custo:
                    for calc in ingredientes:
                        resources[calc] -= ingredientes[calc]
                elif payment > custo:
                    troco = round(payment - custo, 2)
                    print(f"Here if ${troco} dollars in change.")
                    for calc in ingredientes:
                        resources[calc] -= ingredientes[calc]
                print(f"Here is your {order}. Enjoy! ☕")

while not end_turn:
    like = input("What would you like? (espresso/latte/cappuccino)").lower()
    if like == "off":
        end_turn = True
    elif like == "report":
        for item in resources:
            print(f"{item}: {resources[item]}")
    elif like == "espresso":
         check(like)
    elif like == "latte":
        check(like)
    elif like == "cappuccino":
        check(like)
    else:
        print("Please chose a valid option")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
