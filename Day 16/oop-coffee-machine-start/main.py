from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

while 0 == 0:
    UserChoice = input("What would you like (espresso/latte/cappuccino): ")

    if UserChoice == "report":
        CoffeeMaker.report()
    elif UserChoice == "off":
        quit()
    else:
        CoffeeMaker.make_coffee(UserChoice)
