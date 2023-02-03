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
              "wholemeal": 1,
              "white": 0.8,
              "cheesy white": 1.2,
              "gluten free": 1.40
              }
    meats = {"name": "meats",
             "chicken": 2.69,
             "beef": 3,
             "salami": 4,
             "vegan slice": 3.3
             }
    garnishes = {"name": "garnishes",
                 "onion": 1.69,
                 "tomato": 1,
                 "lettuce": 2,
                 "cheese": 2.50
                 }

    bread = get_option(breads)
    meat = get_option(meats)
    garnish = get_option(garnishes)
    total_cost = breads[bread] + meats[meat] + garnishes[garnish]
    print("Order Summary:")
    print(f"Bread: {bread.title()}")
    print(f"Meat: {meat.title()}")
    print(f"Garnish: {garnish.title()}")
    print(f"Cost: ${total_cost:.2f}")
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


def get_option(menu):
    # This function eliminates the need to repeat code, since the only
    # difference is the ingredient names
    menu_name = menu["name"]
    # added attribute to each menu so it can be referenced by name
    print(f"Available {menu_name}:")
    print("\n".join([item.title() for item in menu][1:]))
    # Displaying menu so that each item is displayed on one line
    while True:
        choice = input(f"\nWhich of these {menu_name} do you want: ").lower()
        if menu.get(choice) is None:  # if the user's choice isn't in the menu
            print("Sorry, that isn't a valid choice, please see above"
                  " for a list of available items")
        else:
            return choice


if __name__ == "__main__":
    main()
