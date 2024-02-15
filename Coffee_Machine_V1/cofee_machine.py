from menu import MENU, resources

class CoffeeMachine():
    def __init__(self, water, milk, coffee, money=0):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money
    
    def imprimir_reporte(self):
        print(f'Water: {self.water}')
        print(f'Milk: {self.milk}')
        print(f'Coffee: {self.coffee}')
        print(f'Money: {self.money}')
    
    def cobrar(self, costo):
        self.money += costo
    
    def hacer_bebida(self, bebida):
        drink_key = MENU[bebida]
        ingredients = drink_key['ingredients']

        water = ingredients['water']
        coffee = ingredients['coffee']
        cost = drink_key['cost']

        # Verificar si hay suficientes recursos
        if self.water >= water and self.coffee >= coffee:
            self.water -= water
            self.coffee -= coffee
            self.cobrar(cost)
            print(f"Here is your {bebida}. Enjoy!")
        else:
            print("Sorry, not enough resources to make the drink.")

new_coffee_machine = CoffeeMachine(resources['water'], resources['milk'], resources['coffee'])

while True:
    accion = input('“What would you like? (espresso/latte/cappuccino): ').lower()
    while accion not in ['espresso', 'latte', 'cappuccino', 'report', 'off']:
        print("Please enter a valid response (y/n).")
        seguir_jugando = input('What would you like? (espresso/latte/cappuccino): ')
    
    if accion == 'off':
        break
    elif accion == 'report':
        new_coffee_machine.imprimir_reporte()
    elif accion in ['espresso', 'latte', 'cappuccino']:
        new_coffee_machine.hacer_bebida(accion)

print(MENU['espresso'])