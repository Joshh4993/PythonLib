import sys
import random
import json

def get_stock_data():
    with open('inventory.json') as vending_file:
        stock_data = json.load(vending_file)
        return stock_data

def get_stock_from_selection(selection_id):
    stock_data = get_stock_data()
    stock = stock_data[f'{selection_id}']
    return stock

def take_away_from_stock_by_selection(selection_id, amount):
    stock_data = get_stock_data()
    objectToEdit = stock_data[f'{selection_id}']
    in_stock_amount = objectToEdit['item_amount']
    new_stock_amount = in_stock_amount - amount
    objectToEdit['item_amount'] = new_stock_amount
    stock_data[f'{selection_id}'] = objectToEdit
    jsonFile = open('inventory.json', 'w+')
    jsonFile.write(json.dumps(stock_data))
    jsonFile.close()
    return
