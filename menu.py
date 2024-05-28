# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Set up order list
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Continuous loop to handle multiple orders
while True:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order?")
    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first-level dictionary items in menu)
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number and a valid menu option
    if menu_category.isdigit() and int(menu_category) in menu_items.keys():
        # Save the menu category name to a variable
        menu_category_name = menu_items[int(menu_category)]

        # Print out the menu category name they selected
        print(f"You selected {menu_category_name}")

        # Print out the menu options from the menu_category_name
        print(f"What {menu_category_name} item would you like to order?")
        i = 1
        menu_items = {}
        print("Item # | Item name                | Price")
        print("-------|--------------------------|-------")
        for key, value in menu[menu_category_name].items():
            # Check if the menu item is a dictionary to handle differently
            if type(value) is dict:
                for key2, value2 in value.items():
                    num_item_spaces = 24 - len(key + key2) - 3
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                    menu_items[i] = {"Item name": key + " - " + key2, "Price": value2}
                    i += 1
            else:
                num_item_spaces = 24 - len(key)
                item_spaces = " " * num_item_spaces
                print(f"{i}      | {key}{item_spaces} | ${value}")
                menu_items[i] = {"Item name": key, "Price": value}
                i += 1

        # Ask customer to input menu item number
        menu_item = input("Type menu item number: ")

        # Check if the customer typed a number and it's a valid menu item
        if menu_item.isdigit() and int(menu_item) in menu_items.keys():
            # Store the item name as a variable
            menu_item_name = menu_items[int(menu_item)]

            # Ask customer for the quantity of the menu item
            quantity = input("How many of this item would you like to order? ")

            # Check if the quantity is a number and greater than 0
            if quantity.isdigit():
                quantity = int(quantity)
                if quantity > 0:
                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                        "Item name": menu_item_name["Item name"],
                        "Price": menu_item_name["Price"],
                        "Quantity": quantity
                    })

                    # Ask if they want to order more items or place the order
                    more_order = input("Do you want to order more items? (yes/no): ").lower()
                    if more_order != "yes":
                        break
                else:
                    print("Invalid quantity. Please enter a number greater than 0.")
            else:
                print("Invalid input for quantity. Please enter a valid number.")
        else:
            print("Invalid menu item number. Please choose a valid menu item.")
    else:
        print("Invalid menu category number. Please choose a valid menu category.")

# Print the final order receipt
print("\nYour order:")
total_cost = 0
for item in order_list:
    item_total = item["Price"] * item["Quantity"]
    total_cost += item_total
    print(f"{item['Quantity']}x {item['Item name']} - ${item_total:.2f}")

print(f"Total cost: ${total_cost:.2f}")

