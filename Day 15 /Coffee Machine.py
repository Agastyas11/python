from collections import Counter

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}


def money_exchange(drink_choice):
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total_payment = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)

    if MENU[drink_choice]["cost"] > total_payment:
        print("Sorry that's not enough money. Money refunded.")
    elif MENU[drink_choice]["cost"] <= total_payment:
        change = total_payment - int(MENU[drink_choice]["cost"])
        if change > 0:
            print(f"Here is {round(change, 2)} dollars in change.")
        resources["money"] += MENU[drink_choice]["cost"]
        print(f"Here is your {drink_choice}. Enjoy!")


def drink_exchange(drink_choice):
    drink_ingredients = Counter(MENU[drink_choice]["ingredients"])
    total_resources = Counter(resources)

    if resources["water"] < MENU[drink_choice]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    elif resources["coffee"] < MENU[drink_choice]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
    elif resources["milk"] < MENU[drink_choice]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    else:
        return total_resources - drink_ingredients


while 0 == 0:
    UserChoice = input("What would you like (espresso/latte/cappuccino): ")

    if UserChoice == "report":
        [print(f"{key}: {value}") for key, value in resources.items()]
    elif UserChoice == "off":
        quit()
    else:
        resources = drink_exchange(UserChoice)
        money_exchange(UserChoice)
    