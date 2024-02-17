from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

money_machine.report()
coffee_maker.report()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f'What would you like? {options}: ').lower()

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None: # Condición que decidí agregar para en caso de que se ingrese una clave no esperada no de errores.
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)