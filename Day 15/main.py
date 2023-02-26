import time

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
    "money": 0
}


def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def take_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    result = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    return result


def check_transaction(money, drink_cost):
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f"Here is ${change} in change.")
        resources["money"] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print("Your coffe is being prepared. Please wait a second.")
    time.sleep(3)
    result = f"Here is your {drink_name} ☕. Enjoy!"
    return result


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Bye!")
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            money = take_money()
            if check_transaction(money, drink["cost"]):
                print(make_coffee(choice, drink["ingredients"]))
