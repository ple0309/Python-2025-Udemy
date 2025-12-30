MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

def make_coffee(drink):
    """It will calculate resources and update again."""
    for key in resources:
        if key in drink['ingredients']:
            resources[key] -= drink['ingredients'][key]

def print_report(total_money):
    """Print out the list of resources and money."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${total_money}")

def check_resource(drink):
    """If resource is enough to make the drink it will return True. Otherwise, return False"""
    ingredient = drink['ingredients']
    for key in resources:
        if key in ingredient and resources[key] < ingredient[key]:
            print(f"Sorry we don't have enough {key}.")
            return False
    return True

def insert_coin():
    """Taking the input from user"""
    print("Please insert coins.")
    quarter = int(input("how many quarters?: "))
    dime = int(input("how many dimes?: "))
    nickle = int(input("how many nickles?: "))
    penny = int(input("how many pennies?: "))
    return quarter, dime, nickle, penny

def total_coins(quarter, dime, nickle, penny):
    """Calculating for the total money"""
    result = (0.25 * quarter) + (0.1 * dime) + (0.05 * nickle) + (0.01 * penny)
    return result

def check_money(total_money, cost):
    """Checking whether the input coins is enough to get the order or not."""
    if total_money < cost:
        return False
    return True

money = 0.0

should_continue = True
while should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice in ['espresso','latte','cappuccino']:
        drink = MENU[choice]
        if check_resource(drink):
            quarters, dimes, nickles, pennies = insert_coin()
            total = total_coins(quarters, dimes, nickles, pennies)
            if check_money(total, drink['cost']):
                make_coffee(drink)
                money += drink['cost']
                change = total - drink['cost']
                print(f"Here is ${change:.2f} in change.")
                print(f"Here is your {choice}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
    elif choice == 'report':
        print_report(money)
    elif choice == 'off':
        should_continue = False
    else:
        print("Please choice correct options.")
