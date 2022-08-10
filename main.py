import sys
from data import drinks
from data import coins

resource = {
    "water": 100,
    "milk": 50,
    "coffee": 76,
    "money": 2.5
}


def if_sufficient(coffee) -> bool:
    ingredients = drinks[coffee]["ingredients"].keys()
    for ingredient in ingredients:
        if not drinks[coffee]["ingredients"][ingredient] < resource[ingredient]:
            print(f"Sorry, there is not enough {ingredient}")
            return False
    return True


def work_on_order(coffee):
    resource["water"] -= drinks[coffee]["ingredients"]["water"]
    resource["milk"] -= drinks[coffee]["ingredients"]["milk"]
    resource["water"] -= drinks[coffee]["ingredients"]["water"]
    resource["money"] += drinks[coffee]["cost"]

    print(f"Here is your {coffee}, Enjoy!")


def display_report():
    print(f'Water: {resource["water"]}ml')
    print(f'Milk: {resource["milk"]}ml')
    print(f'Coffee: {resource["coffee"]}g')
    print(f'Money: ${round(resource["money"], 2)}')


def input_filter(ip_string) -> str:
    if ip_string == "off":
        sys.exit()
    elif ip_string == "report":
        display_report()
    return ip_string


def coin_insert() -> float:
    print("Please insert coins.")
    quarters = coins["quarter"] * int(input_filter(input("Quarters : ")))
    nickles = coins["nickle"] * int(input_filter(input("Nickles : ")))
    dimes = coins["dime"] * int(input_filter(input("Dimes : ")))
    pennies = coins["penny"] * int(input_filter(input("Pennies : ")))

    return quarters + nickles + dimes + pennies


def main():
    coffee = input_filter(input("What would you like? (espresso/latte/cappuccino): "))
    if coffee == "report":
        return

    if not if_sufficient(coffee):
        return

    coin_processed = coin_insert()

    if coin_processed < drinks[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return

    work_on_order(coffee)

    if coin_processed > drinks[coffee]["cost"]:
        print(f'Here is ${round(coin_processed - drinks[coffee]["cost"], 2)} dollars in change')


while True:
    main()
