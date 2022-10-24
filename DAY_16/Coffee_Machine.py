from menu import Menu, MenuItem
from Coffee_maker import CoffeeMaker
from Money_machine import MoneyMachine

machine_running = True

coffee_maker = CoffeeMaker()
money = MoneyMachine()
menu = Menu()

while machine_running:
    option = menu.get_items()
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        machine_running = False
    elif choice == "report":
        money.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)




