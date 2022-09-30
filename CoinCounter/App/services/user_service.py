import bcrypt
import services.database_service as db

salt = bcrypt.gensalt()

def update_volunteer(username, key, value):
    volunteer_data, stats_data, coin_data = db.load_databases()
    username = username.lower()

    # Check username exists
    if volunteer_data.get(username):
        user_data = volunteer_data.get(username)
        user_data[f'{key}'] = value
        db.save_database(db_name='volunteers', db_key=username, db_file=user_data)
        return True
    else: 
        return False

def register_volunteer(username, name, password):
    volunteer_data, stats_data, coin_data = db.load_databases()
    username = username.lower()

    #Check Username is not taken
    if (volunteer_data.get(username) is None):
        # If username is NOT taken then vvv
        #print("Okay to create acc") - Debug Statement

        #Check if 3 users are registered - if so, deny acc. creation
        db_users_count = 0
        for key, value in volunteer_data.items():
            db_users_count = db_users_count + 1
        if db_users_count >= 3:
            return_value = "ACCS"
            username = ""
            return return_value, username

        #Encode and Hash Password
        password = password.encode('utf-8')
        hashedPassword = bcrypt.hashpw(password, salt)
        db_key = username
        db_value = {
            "name" : f"{name}",
            "password" : f"{hashedPassword}",
            "accuracy": "100.00",
            "bags_checked" : 0,
            "bags_correct" : 0,
            "last_session" : "HAS NOT LOGGED IN"
        }
        return_value = True
        db.save_database(db_name='volunteers', db_key=db_key, db_file=db_value)

        return return_value, username
    else:
        # If username is taken then vvv
        #print("Taken user") - Debug Statement
        return_value = False
        username = ""
        return return_value, username

def login_volunteer(username, password):
    volunteer_data, stats_data, coin_data = db.load_databases()
    username = username.lower()

    #Check Username exists
    if volunteer_data.get(username):
        # If username is NOT taken then vvv
        #print("Okay to create acc") - Debug Statement

        password = password.encode('utf-8')
        user = volunteer_data.get(username)
        hashed = user['password']
        hashed = hashed.strip("")
        hashed = hashed.lstrip('b')
        hashed = hashed.strip("'")
        hashed = hashed.encode('utf-8')
        if bcrypt.hashpw(password, hashed) == hashed:
            return_value = True
            username = f"{username}"
            return return_value, username
        else:
            return_value = False
            username = ""
            return return_value, username
    else:
        # If username is taken then vvv
        #print("Taken user") - Debug Statement
        return_value = False
        username = ""
        return return_value, username