# # from prettytable import PrettyTable


# # table = PrettyTable()
# # table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# # table.add_column("Type", ["Electric", "Water", "Fire"])
# # table.align = "l"

# # print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_is_on = True

while machine_is_on:
    prompt = input(f"What do you want?: {menu.get_items()}")
    if prompt == "off":
        print("Device successfully turned off!")
        machine_is_on = False
    elif prompt == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(prompt)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)