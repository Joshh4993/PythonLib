import services.database_service as db
import services.user_service as users

def save_log_file():
    volunteer_data, stats_data, coin_data = db.load_databases()
    file_lines = []
    file_lines.append("----------------------------------------------------")
    file_lines.append(f"Accurate as of: {stats_data['last_update']}")
    file_lines.append("----------------------------------------------------")
    file_lines.append("Statistics:")
    file_lines.append(f"    Accuracy: {stats_data['total_accuracy']}")
    file_lines.append(f"    Total Bags Checked: {stats_data['total_bags_checked']}")
    file_lines.append(f"    Total Correct: {stats_data['total_correct']}")
    file_lines.append(f"    Total Incorrect:  {stats_data['total_bags_checked'] - stats_data['total_correct']}")
    file_lines.append("----------------------------------------------------")
    file_lines.append("Volunteers:")
    for key, value in volunteer_data.items():
        file_lines.append(f"    {value['name']}:")
        file_lines.append(f"        Accuracy: {value['accuracy']}")
        file_lines.append(f"        Bags Checked: {value['bags_checked']}")
        file_lines.append(f"        Correct: {value['bags_correct']}")
        file_lines.append(f"        Incorrect: {value['bags_checked'] - value['bags_correct']}")
        file_lines.append(f"        Last Session: {value['last_session']}")
    file_lines.append("----------------------------------------------------")
    with open('./data/CoinCount.txt', 'w') as f:
        f.write('\n'.join(file_lines))

def verify_bag(username, coin_type, bag_weight):
    try:
        volunteer_data, stats_data, coin_data = db.load_databases()
        if (volunteer_data.get(username) is None):
            return_value = False
            corrected_weight = ""
            return return_value, corrected_weight
        else:
            coin_weights = coin_data.get('coin_weights')
            if (coin_weights.get(coin_type) is None):
                return_value = False
                corrected_weight = ""
                return return_value, corrected_weight
            else:
                coin_weight = coin_data['coin_weights']
                bag_values = coin_data['bag_values']
                number_of_expected_coins = int(bag_values[coin_type])
                coin_weight = int(coin_weight[coin_type])
                coin_weight = coin_weight / 100
                bag_weight = bag_weight / 100
                number_of_coins = (bag_weight / coin_weight)

                if (number_of_expected_coins > number_of_coins):
                    # Calculate Adjustment needed
                    adjustment = int(number_of_expected_coins - number_of_coins)
                    add_remove = "ADD"

                    # Add to Users & Overall total checked amount, do not add to correct amount
                    incorrect_bag(username)
                    return add_remove, adjustment
                elif (number_of_coins > number_of_expected_coins):
                    # Calculate adjustment needed
                    adjustment = int(number_of_coins - number_of_expected_coins)
                    add_remove = "REMOVE"

                    # Add to Users & Overall total checked amount, do not add to correct amount
                    incorrect_bag(username)
                    return add_remove, adjustment
                else:
                    adjustment = 0
                    add_remove = "CORRECT"
                    # Bag is Correct = Add to overall totals and user totals
                    correct_bag(username)
                    return add_remove, adjustment
    except ValueError:
        print(ValueError)


def correct_bag(username):
    volunteer_data, stats_data, coin_data = db.load_databases()
    user_data = volunteer_data.get(username)
    total_checked = stats_data['total_bags_checked']
    total_correct = stats_data['total_correct']
    user_checked = user_data['bags_checked']
    user_correct = user_data['bags_correct']
    total_checked = total_checked + 1
    total_correct = total_correct + 1
    user_checked = user_checked + 1
    user_correct = user_correct + 1

    total_accuracy = calculate_accuracy(
        checked=total_checked, correct=total_correct)
    user_accuracy = calculate_accuracy(
        checked=user_checked, correct=user_correct)

    users.update_volunteer(
        username=username, key='bags_checked', value=user_checked)
    users.update_volunteer(
        username=username, key='bags_correct', value=user_correct)
    users.update_volunteer(
        username=username, key='accuracy', value=user_accuracy)

    db.save_database(db_name='total_stats',
                     db_key='total_bags_checked', db_file=total_checked)
    db.save_database(db_name='total_stats',
                     db_key='total_correct', db_file=total_correct)
    db.save_database(db_name='total_stats',
                     db_key='total_accuracy', db_file=total_accuracy)


def incorrect_bag(username):
    volunteer_data, stats_data, coin_data = db.load_databases()
    user_data = volunteer_data.get(username)
    total_checked = stats_data['total_bags_checked']
    total_correct = stats_data['total_correct']
    user_checked = user_data['bags_checked']
    user_correct = user_data['bags_correct']
    total_checked = total_checked + 1
    user_checked = user_checked + 1

    total_accuracy = calculate_accuracy(
        checked=total_checked, correct=total_correct)
    user_accuracy = calculate_accuracy(
        checked=user_checked, correct=user_correct)

    users.update_volunteer(
        username=username, key='bags_checked', value=user_checked)
    users.update_volunteer(
        username=username, key='accuracy', value=user_accuracy)

    db.save_database(db_name='total_stats',
                     db_key='total_bags_checked', db_file=total_checked)
    db.save_database(db_name='total_stats',
                     db_key='total_accuracy', db_file=total_accuracy)


def calculate_accuracy(checked, correct):
    accuracy = (correct / checked) * 100
    format_accuracy = "{:.2f}".format(accuracy)
    return format_accuracy

