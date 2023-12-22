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

resources["Money"] = 0

type =["ml", "ml", "g"]


def buy_drink(drink):
    """This function is used to check the coins that the user insert and checks if there is enough money for buy the
    drinks"""
    quarters = int(input("How many quarters?: "))
    quarters *= 0.25
    dimes = int(input("How many dimes?: "))
    dimes *= 0.1
    nickels = int(input("How many nickles?: "))
    nickels *= 0.05
    pennies = int(input("How many pennies?: "))
    pennies *= 0.01
    coins_user = quarters + dimes + nickels + pennies
    # Checks if there is enough coins for the drink cost
    if coins_user < MENU[f"{drink}"]["cost"]:
        print("Sorry there is enough")
        print(f"Your coins: {coins_user}")
    else:
        resources["Money"] += MENU[f"{drink}"]["cost"]
        # print(f"{coins_user} - {MENU[f'{drink}']['cost']}")
        coins_user = round(coins_user - MENU[f"{drink}"]["cost"], 2)
        print("You coffe ☕")
        print(f"You change {coins_user}")
        coins_user = 0
        # print(f"The coins user is {coins_user}")


def i_coffe(drink):
    """This function verify if there is enough coffee, Take the drink and their ingredients"""
    if MENU[f"{drink}"]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry theres is enough coffee")
    else:
        return True


def i_water(drink):
    """This function verify if there is enough water, Take the drink and their ingredients"""
    if MENU[f"{drink}"]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is enough water")
    else:
        return True


def i_milk(drink):
    """This function verify if there is enough milk, Take the drink and their ingredients"""
    if MENU[f"{drink}"]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is enough milk")
    else:
        return True


machine_on = True
while machine_on:
    coffe = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffe == 'espresso':
        # pass
        # print(MENU["espresso"]["ingredients"]["water"])
        # resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        if i_water(coffe) and i_coffe(coffe):
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            buy_drink(coffe)
    elif coffe == 'latte':
        if i_water(coffe) and i_coffe(coffe) and i_milk(coffe):
            resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
            buy_drink(coffe)

    elif coffe == 'cappuccino':
        if i_water(coffe) and i_coffe(coffe) and i_milk(coffe):
            resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
            resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
            resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
            buy_drink(coffe)
    elif coffe == 'report':
        position = 0
        for name in resources:
            if name == 'Money':
                print(f"{name}: $ {resources[f'{name}']}")
            else:
                print(f"{name}: {resources[f'{name}']} {type[position]}")
                position += 1

    elif coffe == 'off':
        print("See you.")
        machine_on = False
    else:
        print("You don't choice a valid option.")
