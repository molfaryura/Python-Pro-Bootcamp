from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()

while True:
    order = input(f"What do you want to order? ({my_menu.get_items()}): ").lower()
    if order == "off":
        print("Bye!")
        break
    elif order == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(order)
        if my_coffee_maker.is_resource_sufficient(drink=drink):
            if my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)
