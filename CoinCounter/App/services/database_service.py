import json

def load_databases():
    with open('./data/volunteers.json') as volunteer_file:
        volunteer_data = json.load(volunteer_file)
        with open('./data/total_stats.json') as stats_file:
            stats_data = json.load(stats_file)
            with open('./data/coin_data.json') as coin_file:
                coin_data = json.load(coin_file)
                return volunteer_data, stats_data, coin_data
        
def save_database(db_name, db_key, db_file):
    try:
        with open(f'./data/{db_name}.json', 'r') as f:
            data = json.loads(f.read())
        
        data[f'{db_key}'] = db_file

        with open(f'./data/{db_name}.json', 'w') as f:
            f.write(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))
        
        return True
    except:
        print("Error Saving DB")
        return False