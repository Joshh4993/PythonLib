from vend_utils import *
import sys

welcome_brief = "Hello there!\nWelcome to the best vending machine with the worst language, (that's definitely a joke); anyways, here's our selection."
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
    selection_chosen = input("Please choose an option to learn more: ")
    if selection_chosen in selections_data:
        give_user_info_about_selection(selection_chosen)
    else:
        print("This option does not exist, please try again.")
        ask_for_selection()
        
def give_user_info_about_selection(selection_chosen):
    stock_info = get_stock_from_selection(selection_id=selection_chosen)
    item_value = calculate_price_from_selection(selection_id=selection_chosen)
    item_cost = stock_info['item_cost']
    item_name = stock_info['item_brand_name']
    item_amount = stock_info['item_amount']
    if item_amount is 0:
        print("This item is out of stock, please select another option.")
        ask_for_selection()
    else:
        print(f"Item Information:\nName: {item_name}\nCost: {item_value}")
        validation_option = input("If this what you want, please type 'y', otherwise type 'n': ")
        validation_option.lower()
        match validation_option:
            case "y":
                ask_for_money(selection_chosen=selection_chosen, item_amount=item_cost)
            case _:
                print("I see you are not happy with this item. Returning to menu.")
                ask_for_selection()

def ask_for_money(selection_chosen, item_amount):
    print(f"Your selection is {selection_chosen}")
    formatted_item_amount = format_currency_from_float(item_cost=item_amount)
    change_inserted = float(input(f"The item is {formatted_item_amount}, please enter your change: "))
    change_difference = calculate_change(money_inserted=change_inserted, item_value=item_amount)
    formatted_change = format_currency_from_float(item_cost=change_difference)
    if change_difference > 0:
        print(f"We are dispensing your item and change, your change is: {formatted_change}")
        take_away_from_stock_by_selection(selection_id=selection_chosen, amount=1)
    else:
        print(
            f"Uh oh! You inserted {change_inserted}, this was not enough. Returning change.")
        ask_for_money(selection_chosen, item_amount)
        
welcome_message()