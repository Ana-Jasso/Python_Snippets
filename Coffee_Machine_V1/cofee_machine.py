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
    
    def cobrar(self, bebida):
        drink_key = MENU[bebida]
        cost = drink_key['cost']
        self.money += cost
    
    def obtener_cambio(self, bebida, dinero):
        drink_key = MENU[bebida]
        cost = drink_key['cost']
        return dinero - cost
    
    def hacer_bebida(self, bebida):
        if bebida not in MENU:
            print("Sorry, that item is not available.")
            return

        drink_key = MENU[bebida]
        ingredients = drink_key['ingredients']

        water = ingredients['water']
        milk = ingredients['milk']
        coffee = ingredients['coffee']

        # Verificar si hay suficientes recursos
        if self.water >= water and self.coffee >= coffee and self.milk >= milk:
            self.water -= water
            self.milk -= milk
            self.coffee -= coffee

            # Cobrar solo si hay suficientes recursos
            self.cobrar(bebida)
            print(f'Your change is ${cambio:.2f}.')
            print(f"Here is your {bebida}. Enjoy!")
        
        else:
            print("Sorry, not enough resources to make the drink.")

def solicitar_dinero():
    try:
        quarters = int(input('How many quarters?: ')) * 0.25
        dimes = int(input('How many dimes?: ')) * 0.10
        nickels = int(input('How many nickels?: ')) * 0.05
        pennies = int(input('How many pennies?: ')) * 0.01
    except ValueError:
        print("Please enter a valid number.")
        return solicitar_dinero()  # Recursively call the function to retry
    
    return quarters + dimes + nickels + pennies

new_coffee_machine = CoffeeMachine(resources['water'], resources['milk'], resources['coffee'])

while True:
    accion = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if accion == 'off':
        break
    elif accion == 'report':
        new_coffee_machine.imprimir_reporte()
    elif accion in ['espresso', 'latte', 'cappuccino']:
        dinero_ingresado = solicitar_dinero()
        cambio = new_coffee_machine.obtener_cambio(accion, dinero_ingresado)

        while cambio < 0:
            print(f'You entered not enough money. You need ${abs(cambio):.2f} more.')
            dinero_ingresado = solicitar_dinero()
            cambio = new_coffee_machine.obtener_cambio(accion, dinero_ingresado)

        new_coffee_machine.hacer_bebida(accion)