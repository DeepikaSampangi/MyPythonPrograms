from coffee_menu import MENU, resource_details, dollar_value


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
            items_unavail.append(MENU[type]["ingredients"][item])
        return items_unavail


def make_coffee(type):
    for item in MENU[type]["ingredients"]:
        resource_details[item]["qty"] -= MENU[type]["ingredients"][item]

def handle_payment(type, paid):
    resource_details["Money"]["qty"] += MENU[type]["cost"]

def coffee_machine(type, paid):
    items_unavail = get_unavilable(type)
    if items_unavail:
        print("Sorry we are short of")
        for item in items_unavail:
            print(item)
    else:
        make_coffee(type)
        handle_payment(type, paid)


# user_choice = input("What would you like? (espresso/latte/cappuccino): ")

# if user_choice == "espresso":
#     #make espresso
# elif user_choice == "latte":
#     #make latte
# elif user_choice == "cappuccino":
#     #make cappuccino
# else:
#     print("Turned off")
