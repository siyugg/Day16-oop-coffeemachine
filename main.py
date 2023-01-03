from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino/):")
    if order == 'off':
        machine_on = False
    elif order == str('report'):
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            cost = drink.cost
            print(f"Please pay ${cost}")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



