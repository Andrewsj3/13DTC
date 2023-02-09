"""sandwich.py: This program allows the user to choose ingredients for
their sandwich. When the user has finished, the program prints the order
and the cost. The user can then choose to confirm or alter their order.
Jack Andrews
03/02/23
"""


def main():
    print("Welcome to the sandwich store!")
    order()


def order():
    breads = {"name": "breads",
              ("wholemeal", "wh"): 1,
              ("white", "w"): 0.8,
              ("cheesy white", "c"): 1.2,
              ("gluten free", "gf"): 1.40
              }
    meats = {"name": "meats",
             ("chicken", 'c'): 2.69,
             ("beef", 'b'): 3,
             ("salami", 's'): 4,
             ("vegan slice", 'vs'): 3.3
             }
    garnishes = {"name": "garnishes",
                 ("onion", 'o'): 1.69,
                 ("tomato", 't'): 1,
                 ("lettuce", 'l'): 2,
                 ("cheese", 'c'): 2.50
                 }
    total_cost = [0]
    order = []
    bread = get_option(breads, total_cost, order)
    while True:
        choice = input(
            "Do you want to: add meat, add garnish,"
            " or finish order? (m/g/f) ").lower()
        if choice == 'm':
            meat = get_option(meats, total_cost, order)
        elif choice == 'g':
            garnish = get_option(garnishes, total_cost, order)
        elif choice == 'f':
            break
        else:
            print("Invalid choice, please enter again.")
    print("Order Summary:")
    print(order[0] + " bread")
    for item in order[1:]:
        print(item)
    print(f"Total cost: ${total_cost[0]:.2f}")
    # This is so the user can make sure they ordered what they wanted
    confirm()


def confirm():
    while True:
        purchase = input(
            "Do you want to proceed with the purchase? (y/n) ").lower()
        if purchase == 'y':
            print("Thank you for your purchase!")
            exit()
        elif purchase == 'n':
            while True:
                choice = input("Do you want to make a change"
                               " or exit? (c/e) ").lower()
                if choice == 'c':
                    order()
                elif choice == 'e':
                    print("See you soon!")
                    exit()
                else:
                    print("Invalid choice, please enter c or e")
        else:
            print("Invalid choice, please enter y or n")


def get_option(menu, total_cost, order):
    # This function eliminates the need to repeat code, since the only
    # difference is the ingredient names
    menu_name = menu["name"]
    # added attribute to each menu so it can be referenced by name
    print(f"Available {menu_name}:")
    print("\n".join(
        [item[0].title() + f" ({item[1].title()})" for item in menu][1:]))
    # Displaying menu so that each item is displayed on one line
    while True:
        choice = input(f"\nWhich of these {menu_name} do you want: ").lower()
        if (cost := get_choice(
                menu, choice, order)) is None:
            # if the user's choice isn't in the menu
            print("Sorry, that isn't a valid choice, please see above"
                  " for a list of available items")
        else:
            total_cost[0] += cost
            return choice


def get_choice(menu, choice, order):
    for item in menu:
        if choice in item:
            order.append(item[0].title())
            return menu[item]
    return None


if __name__ == "__main__":
    main()
