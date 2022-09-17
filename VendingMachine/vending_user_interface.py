from vend_utils import *
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Vending Machine")
ascii_separator = "-" * 50
ascii_separator_80 = "-" * 77
welcome_brief = "Hello there!\nWelcome to the best vending machine with the worst language, (that's definitely a joke); anyways, here's our selection."
selections_data = get_selection_options()

def welcome_message():
    print(ascii_separator_80)
    print(ascii_banner)
    print(ascii_separator_80)
    print(welcome_brief)
    for key in selections_data:
        print(f'{key}')
    ask_for_selection()

def ask_for_selection():
    input_selection_chosen = input("Please choose an option to learn more: ")
    selection_chosen = input_selection_chosen.upper()
    if selection_chosen in selections_data:
        print(ascii_separator)
        give_user_info_about_selection(selection_chosen)
    else:
        print("This option does not exist, please try again.")
        print(ascii_separator)
        ask_for_selection()
        
def give_user_info_about_selection(selection_chosen):
    stock_info = get_stock_from_selection(selection_id=selection_chosen)
    item_value = calculate_price_from_selection(selection_id=selection_chosen)
    item_cost = stock_info['item_cost']
    item_name = stock_info['item_brand_name']
    item_amount = stock_info['item_amount']
    if item_amount == 0:
        print("This item is out of stock, please select another option.")
        print(ascii_separator)
        ask_for_selection()
    else:
        print(f"Item Information:\nName: {item_name}\nCost: {item_value}")
        validation_option = input("If this what you want, please type 'y', otherwise type 'n': ")
        validation_option.lower()
        match validation_option:
            case "y":
                print(ascii_separator)
                ask_for_money(selection_chosen=selection_chosen, item_amount=item_cost)
            case _:
                print("I see you are not happy with this item. Returning to menu.")
                print(ascii_separator)
                ask_for_selection()

def ask_for_money(selection_chosen, item_amount):
    print(f"Your selection is {selection_chosen}")
    formatted_item_amount = format_currency_from_float(item_cost=item_amount)
    try:
        change_inserted = float(input(f"The item is {formatted_item_amount}, please enter your change: "))
        change_difference = calculate_change(money_inserted=change_inserted, item_value=item_amount)
        formatted_change = format_currency_from_float(item_cost=change_difference)
        if change_difference >= 0:
            print(f"We are dispensing your item and change, your change is: {formatted_change}")
            take_away_from_stock_by_selection(selection_id=selection_chosen, amount=1)
            welcome_message()
        else:
            print(f"Uh oh! You inserted {change_inserted}, this was not enough. Returning change.")
            print(ascii_separator)
            ask_for_money(selection_chosen, item_amount)
    except ValueError:
        print("Uh oh! Didn't expect that, try again.")
        print(ascii_separator_80)
        ask_for_money(selection_chosen, item_amount)
        
welcome_message()