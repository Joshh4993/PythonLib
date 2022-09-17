import json

def get_stock_data():
    with open('inventory.json') as vending_file:
        stock_data = json.load(vending_file)
        return stock_data

def get_stock_from_selection(selection_id):
    stock_data = get_stock_data()
    stock = stock_data[f'{selection_id}']
    return stock
        
def get_selection_options():
    stock_data = get_stock_data()
    selection_keys = []
    for key in stock_data.keys():
        selection_keys.append(key)
    return selection_keys
        
def rename_item_selection(selection_id, new_name):
    try:
        stock_data = get_stock_data()
        objectToEdit = stock_data[f'{selection_id}']
        objectToEdit['item_brand_name'] = new_name
        stock_data[f'{selection_id}'] = objectToEdit
        jsonFile = open('inventory.json', 'w+')
        jsonFile.write(json.dumps(stock_data))
        jsonFile.close()
        return True
    except:
        print("Error in 'rename_item_selection'")
        return False

def adjust_selection_price(selection_id, new_price):
    try:
        stock_data = get_stock_data()
        objectToEdit = stock_data[f'{selection_id}']
        objectToEdit['item_cost'] = new_price
        stock_data[f'{selection_id}'] = objectToEdit
        jsonFile = open('inventory.json', 'w+')
        jsonFile.write(json.dumps(stock_data))
        jsonFile.close()
        return True
    except:
        print("Error in 'adjust_selection_price'")
        return False

def delete_item_from_system_by_selection(selection_id):
    try:
        stock_data = get_stock_data()
        del stock_data[f'{selection_id}']
        jsonFile = open('inventory.json', 'w+')
        jsonFile.write(json.dumps(stock_data))
        jsonFile.close()
        return True
    except:
        print("Error in 'delete_item_from_system_by_selection'")
        return False

def take_away_from_stock_by_selection(selection_id, amount):
    try:
        stock_data = get_stock_data()
        objectToEdit = stock_data[f'{selection_id}']
        in_stock_amount = objectToEdit['item_amount']
        new_stock_amount = in_stock_amount - amount
        objectToEdit['item_amount'] = new_stock_amount
        stock_data[f'{selection_id}'] = objectToEdit
        jsonFile = open('inventory.json', 'w+')
        jsonFile.write(json.dumps(stock_data))
        jsonFile.close()
        return True
    except:
        print("Error in 'take_away_from_stock_by_selection'")
        return False

def add_to_stock_by_selection(selection_id, amount):
    try:
        stock_data = get_stock_data()
        objectToEdit = stock_data[f'{selection_id}']
        in_stock_amount = objectToEdit['item_amount']
        new_stock_amount = in_stock_amount + amount
        objectToEdit['item_amount'] = new_stock_amount
        stock_data[f'{selection_id}'] = objectToEdit
        jsonFile = open('inventory.json', 'w+')
        jsonFile.write(json.dumps(stock_data))
        jsonFile.close()
        return True
    except:
        print("Error in 'add_to_stock_by_selection'")
        return False

def format_currency_from_float(item_cost):
    formatted_currency = "£{:,.2f}".format(item_cost)
    return formatted_currency

def calculate_price_from_selection(selection_id):
    try:
        stock_data = get_stock_data()
        selected_item = stock_data[f'{selection_id}']
        item_cost = selected_item['item_cost']
        formatted_cost = format_currency_from_float(item_cost)
        return formatted_cost
    except:
        print("Error in 'calculate_price_from_selection'")

def calculate_change(money_inserted, item_value):
    change_amount = money_inserted - item_value
    return change_amount