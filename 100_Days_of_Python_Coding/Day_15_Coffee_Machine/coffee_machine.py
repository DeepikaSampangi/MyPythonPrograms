from coffee_menu import MENU, resource_details


def print_report():
    for resource in resource_details:
        print(
            f'{resource}: {resource_details[resource]["qty"]}{resource_details[resource]["metric"]}'
        )


def get_unavilable(type):
    items_unavail = []
    for item in MENU[type]["ingredients"]:
        if MENU[type]["ingredients"][item] < resource_details[item]["qty"]:
            continue
        else:
            items_unavail.append(item)
        return items_unavail


def make_coffee(type):
    for item in MENU[type]["ingredients"]:
        resource_details[item]["qty"] -= MENU[type]["ingredients"][item]
    print(f"Here is your {type}. Enjoy!")


def handle_payment(cost, qt, dimes, nickels, pennies):
    payment_in_dollars = qt * 0.25 + dimes * 0.1 + nickels * 0.5 + pennies * 0.01
    if cost < payment_in_dollars:
        items_unavail = get_unavilable(type)
        if items_unavail:
            print("Sorry we are short of")
            for item in items_unavail:
                print(item)
            print("Money Refunded")
            return False
        else:
            resource_details["money"]["qty"] += MENU[type]["cost"]
            print(f"Here is {payment_in_dollars-cost} in change")
        return True
    else:
        print("Sorry thats's not enought money. Money Refunded.")
        return False


while True:
    print("Type Report or off for other operations")
    type = input("What would you like? (espresso/latte/cappuccino): ")
    if type == "off":
        break
    elif type in MENU.keys():
        cost = MENU[type]["cost"]
        print(f"Make a payment of ${cost}")
        print("Please insert coins.")
        qt = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        if handle_payment(cost, qt, dimes, nickels, pennies):
            make_coffee(type)
    elif type == "report":
        print_report()
