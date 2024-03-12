2# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
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

order_list = []

print("Welcome to the variety food truck. ")

while True:
    print("From which menu would you like to order? ")
    i = 1
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit() and int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
               
            menu_selection = input("Please enter the item number you would like to order or 'q' to quit:")
            
            if menu_selection.lower() == 'q':
                print("Thank you for visiting. Your receipt is as follows:")
                break
            elif menu_selection.lower() == 'r':
                print ("Printing receipt...")
            elif menu_selection.isdigit() and int(menu_selection) in menu_items:
                selected_item = menu_items[int(menu_selection)]
                selected_quantity = input(f"How many {selected_item} would you like? (Default is 1): ")

                if selected_quantity.isdigit():
                            selected_quantity = int(selected_quantity)
                else:
                            selected_quantity = 1

                order_list.append({
                    "Item name": selected_item["Item name"],
                    "Price": selected_item["Price"],
                    "Quantity": selected_quantity})
            else:
                print(f"{menu_selection} Invalid input. Please try again.")
    else:    
        print("invalid number. Please try again.")
            
    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")
        if keep_ordering.lower() =='n':
            print("Thank you for your order. Goodbye!")
            print("Your order is coming up.\n")
            print("Item name                 | Price  | Quantity")
            print("--------------------------|--------|----------")

            total_cost = 0
            for item in order_list:
                item_name = item["Item name"]
                price = item["Price"]
                quantity = item["Quantity"]

                formatted_item_name = "{:<25}".format(item_name)
                formatted_price = "${:8.2f}".format(float(price))
                formatted_quantity = "{:<10}".format(quantity)
  
                output_string = formatted_item_name + "|" + formatted_price + "|" + formatted_quantity
                print(output_string)
                
                total_cost += float(price) * quantity
            print(f"Total cost: ${total_cost:.2f}")
            break
        elif keep_ordering.lower() == 'y':
            print("Please continue with your order")
            break
        else:
            print("Invalid input. Please try again.")
    
    

