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

machine_on = True
while machine_on:
    coffe = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffe == 'espresso':
        # pass
        # print(MENU["espresso"]["ingredients"]["water"])
        # resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        if MENU["espresso"]["ingredients"]["water"] < resources["water"]:
            pass
        else:
            print(f"Sorry theres is enough {resources}")
    elif coffe == 'latte':
        pass
    elif coffe == 'cappuccino':
        pass
    elif coffe == 'report':
        for name in resources:
            print(f"{name}: {resources[f'{name}']}")
    elif coffe == 'off':
        print("See you.")
        machine_on = False
    else:
        print("You don't choice a valid option.")

