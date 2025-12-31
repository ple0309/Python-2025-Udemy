from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
item = MenuItem("",0,0,0,0)
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

should_continue = True
while should_continue:
    choice = input(f"What would you like? ({menu.get_items()}):").lower()
    if choice == 'off':
        should_continue = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        if menu.find_drink(choice):
            for i in menu.menu:
                if i.name == choice:
                    item = i
            if coffee_maker.is_resource_sufficient(item):
                if money_machine.make_payment(item.cost):
                    coffee_maker.make_coffee(item)
