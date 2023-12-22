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

machine_on = True
while machine_on:
    coins = 0
    coffe = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffe == 'espresso':
        # pass
        # print(MENU["espresso"]["ingredients"]["water"])
        # resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        if MENU["espresso"]["ingredients"]["water"] < resources["water"]:
            if MENU["espresso"]["ingredients"]["coffee"] < resources["coffee"]:
                resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
                quarters = int(input("How many quarters?: "))
                quarters *= 0.25
                dimes = int(input("How many dimes?: "))
                dimes *= 0.1
                nickels = int(input("How many nickles?: "))
                nickels *= 0.05
                pennies = int(input("How many pennies?: "))
                pennies *= 0.01
                coins = quarters + dimes + nickels + pennies
                if coins < MENU["espresso"]["cost"]:
                    print("Sorry there is enough")
                    print(f"Final coins {coins}")
                else:
                    resources["Money"] += MENU["espresso"]["cost"]
                    print(f"{coins} - {MENU['espresso']['cost']}")
                    coins = round(coins - MENU["espresso"]["cost"], 1)
                    print("You coffe ☕")
                    print(f"You change {coins}")
            else:
                print("Sorry there is enough coffee")
        else:
            print("Sorry theres is enough water")
    elif coffe == 'latte':
        if MENU["latte"]["ingredients"]["water"] < resources["water"]:
            if MENU["latte"]["ingredients"]["milk"] < resources["milk"]:
                if MENU["latte"]["ingredients"]["coffee"] < resources["coffee"]:
                    resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                    resources["milk"] = resources["milk"] - MENU["latte"]["ingredients"]["milk"]
                    resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                    quarters = int(input("How many quarters?: "))
                    quarters *= 0.25
                    dimes = int(input("How many dimes?: "))
                    dimes *= 0.1
                    nickels = int(input("How many nickles?: "))
                    nickels *= 0.05
                    pennies = int(input("How many pennies?: "))
                    pennies *= 0.01
                    coins = quarters + dimes + nickels + pennies
                    if coins < MENU["latte"]["cost"]:
                        print("Sorry there is enough")
                        print(f"Final coins {coins}")
                    else:
                        resources["Money"] += MENU["latte"]["cost"]
                        print(f"{coins} - {MENU['latte']['cost']}")
                        coins = round(coins - MENU["latte"]["cost"], 1)
                        print("You coffe ☕")
                        print(f"You change {coins}")

                else:
                    print("There's no enough coffee")
            else:
                print("There's no enough milk")
        else:
            print("There's no enough water")
    elif coffe == 'cappuccino':
        if MENU["cappuccino"]["ingredients"]["water"] < resources["water"]:
            if MENU["cappuccino"]["ingredients"]["milk"] < resources["milk"]:
                if MENU["cappuccino"]["ingredients"]["coffee"] < resources["coffee"]:
                    resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                    resources["milk"] = resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
                    resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                    quarters = int(input("How many quarters?: "))
                    quarters *= 0.25
                    dimes = int(input("How many dimes?: "))
                    dimes *= 0.1
                    nickels = int(input("How many nickles?: "))
                    nickels *= 0.05
                    pennies = int(input("How many pennies?: "))
                    pennies *= 0.01
                    coins = quarters + dimes + nickels + pennies
                    if coins < MENU["cappuccino"]["cost"]:
                        print("Sorry there is enough")
                        print(f"Final coins {coins}")
                    else:
                        resources["Money"] += MENU["cappuccino"]["cost"]
                        print(f"{coins} - {MENU['cappuccino']['cost']}")
                        coins = round(coins - MENU["cappuccino"]["cost"], 1)
                        print("You coffe ☕")
                        print(f"You change {coins}")
                else:
                    print("There's no enough coffee")
            else:
                print("There's no enough milk")
        else:
            print("There's no enough water")
    elif coffe == 'report':
        for name in resources:
            print(f"{name}: {resources[f'{name}']}")
    elif coffe == 'off':
        print("See you.")
        machine_on = False
    else:
        print("You don't choice a valid option.")

