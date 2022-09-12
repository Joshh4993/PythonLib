from vend_utils import *
import sys

ascii_separator = "-" * 50
welcome_brief = "Hello there!\nWelcome to the best vending machine with the worst language, (that's definitely a joke); anyways, here's our Admin Menu."
admin_options = "Options:\ninfo: Do you want to check the item you have selected is correct?\nrename: Change Selection name\nprice_adjust: Change Item Price\ndelete: Remove Selection from system\nstock_in: Add Stock\nstock_out: Remove Stock\nreturn: Go back to selections menu"
selections_data = get_selection_options()


def welcome_message():
    try:
        print(welcome_brief)
        for key in selections_data:
            print(f'{key}')
        ask_for_selection()
    except:
        print("Error in 'welcome_message'")


def ask_for_selection():
    selection_chosen = input("Please choose an option to do admin stuff: ")
    if selection_chosen in selections_data:
        print(ascii_separator)
        ask_for_command(selection_chosen)
    else:
        print("This option does not exist, please try again.")
        ask_for_selection()


def ask_for_command(selection_chosen):
    print(
        f"I see we are going to look at {selection_chosen}, what would you like to do?")
    print(admin_options)
    admin_command_selection = input(
        "Make the choice now, or forever hold your peace: ")
    admin_command_selection.lower()
    match admin_command_selection:
        case "info":
            print(ascii_separator)
            print(f"Retrieving information for [{selection_chosen}]")
            stock_information = get_stock_from_selection(
                selection_id=selection_chosen)
            item_value = stock_information['item_cost']
            item_brand_name = stock_information['item_brand_name']
            item_type = stock_information['item_type']
            item_amount = stock_information['item_amount']
            print(
                f"Display Name: {item_brand_name}\nItem Cost: {item_value}\nItem Type: {item_type}\nAmount in system: {item_amount}")
            next_selection = input(
                "This is what you chose, would you like to continue? Type 'yes' : ")
            next_selection.lower()
            match next_selection:
                case "yes":
                    print("Okay! Showing you the options again.")
                    print(ascii_separator)
                    ask_for_command(selection_chosen)
                case _:
                    print("Got it! Going back to the main menu.")
                    print(ascii_separator)
                    welcome_message()
        case "rename":
            print(ascii_separator)
            next_selection = input(
                f"Are you sure you want to rename [{selection_chosen}] Type 'yes' : ")
            next_selection.lower()
            match next_selection:
                case "yes":
                    new_name = input(
                        f"Awesome! Tell us what [{selection_chosen}] is: ")
                    response = rename_item_selection(
                        selection_id=selection_chosen, new_name=new_name)
                    if response is True:
                        print(
                            f"Success! Item [{selection_chosen}] is now '{new_name}'. Returning to main menu.")
                        print(ascii_separator)
                        welcome_message()
                    else:
                        print(f"There was an error!")
                case _:
                    print("Okayy! Returning to main menu.")
                    print(ascii_separator)
                    welcome_message()
        case "price_adjust":
            print(ascii_separator)
            next_selection = input(
                f"Are you sure you want to adjust the price of [{selection_chosen}] Type 'yes' : ")
            next_selection.lower()
            match next_selection:
                case "yes":
                    new_price = float(
                        input(f"Awesome! Tell us what [{selection_chosen}]'s new cost is: "))
                    response = adjust_selection_price(
                        selection_id=selection_chosen, new_price=new_price)
                    if response is True:
                        print(
                            f"Success! Item [{selection_chosen}] is now '{new_price}'. Returning to main menu.")
                        print(ascii_separator)
                        welcome_message()
                    else:
                        print(f"There was an error!")
                case _:
                    print("Okayy! Returning to main menu.")
                    print(ascii_separator)
                    welcome_message()
        case "delete":
            print(ascii_separator)
            next_selection = input(
                f"Are you sure you want to remove [{selection_chosen}] from the system? THIS CANNOT BE UNDONE. Type 'yes' : ")
            next_selection.lower()
            match next_selection:
                case "yes":
                    response = delete_item_from_system_by_selection(selection_id=selection_chosen)
                    if response is True:
                        print(
                            f"Success! Item [{selection_chosen}] has been removed. Returning to main menu.")
                        print(ascii_separator)
                        welcome_message()
                    else:
                        print(f"There was an error!")
                case _:
                    print("Okayy! Returning to main menu.")
                    print(ascii_separator)
                    welcome_message()
        case "stock_in":
            print(ascii_separator)
            next_selection = input(
                f"Are you sure you want to adjust the stock of [{selection_chosen}] Type 'yes' : ")
            next_selection.lower()
            match next_selection:
                case "yes":
                    adjust_amount = int(
                        input(f"Awesome! Tell us how many of [{selection_chosen}] to add: "))
                    response = add_to_stock_by_selection(
                        selection_id=selection_chosen, amount=adjust_amount)
                    if response is True:
                        print(
                            f"Success! Item [{selection_chosen}] has been updated. Returning to main menu.")
                        print(ascii_separator)
                        welcome_message()
                    else:
                        print(f"There was an error!")
                case _:
                    print("Okayy! Returning to main menu.")
                    print(ascii_separator)
                    welcome_message()
        case "stock_out":
            print(ascii_separator)
            next_selection = input(
                f"Are you sure you want to adjust the stock of [{selection_chosen}] Type 'yes' : ")
            next_selection.lower()
            match next_selection:
                case "yes":
                    adjust_amount = int(
                        input(f"Awesome! Tell us how many of [{selection_chosen}] to remove: "))
                    response = take_away_from_stock_by_selection(
                        selection_id=selection_chosen, amount=adjust_amount)
                    if response is True:
                        print(
                            f"Success! Item [{selection_chosen}] has been updated. Returning to main menu.")
                        print(ascii_separator)
                        welcome_message()
                    else:
                        print(f"There was an error!")
                case _:
                    print("Okayy! Returning to main menu.")
                    print(ascii_separator)
                    welcome_message()
        case _:
            print(ascii_separator)
            ask_for_selection()


welcome_message()
