from tkinter import *
from datetime import datetime
import time
from tkinter.simpledialog import SimpleDialog
import services.coin_service as coins
import services.user_service as users
import services.database_service as db

#add_remove, adjustment = coins.verify_bag("username", "5", 23500)
#print(f"{add_remove} ({adjustment}) coin(s)")

# -----------
# Application
# -----------

window = Tk()

def login_or_register():
    def login_function():
        username = username_field.get()
        password = password_field.get()
        return_value, username = users.login_volunteer(username, password)
        if return_value is True:
            dashboard(username)
        else:
            top_message_label.config(text="Incorrect Credentials", fg='red')

    for widget in window.winfo_children():
        widget.destroy()
    # Initiate UI Elements
    window.geometry('200x190')
    top_message_label = Label(window, text="LOGIN OR REGISTER")
    username_field_label = Label(window, text="Username")
    username_field = Entry(window)
    password_field_label = Label(window, text="Password")
    password_field = Entry(window, show="*")
    login_button = Button(window, text="LOGIN", fg='green', command=login_function)
    register_button = Button(window, text="REGISTER", command=register)

    # Place UI Elements to screen
    top_message_label.config(anchor=CENTER)
    top_message_label.pack(pady=2)
    username_field_label.pack(pady=2)
    username_field.pack(pady=2)
    username_field.focus()
    password_field_label.pack(pady=2)
    password_field.pack(pady=2)
    login_button.pack(pady=1)
    register_button.pack(pady=1)

def register():
    def register_function():
        name = n_name_field.get()
        username = n_username_field.get()
        password = n_password_field.get()
        conf_password = n_conf_password_field.get()

        if password == conf_password:
            return_value, username = users.register_volunteer(username, name, password)
            if return_value is True:
                dashboard(username)
            elif return_value == "ACCS":
                n_top_message_label.config(text="ERROR_ACCS", fg='red')
            else:
                n_top_message_label.config(text="Username Taken", fg='red')
        else:
            n_top_message_label.config(text="Passwords do not match", fg='red')

    for widget in window.winfo_children():
        widget.destroy()
    # Initiate UI Elements
    window.geometry('200x250')
    n_top_message_label = Label(window, text="REGISTER ACCOUNT")
    n_top_message_label.config(anchor=CENTER)
    n_top_message_label.pack(pady=2)
    n_name_field_label = Label(window, text="Name")
    n_name_field = Entry(window)
    n_username_field_label = Label(window, text="Username")
    n_username_field = Entry(window)
    n_password_field_label = Label(window, text="Password")
    n_password_field = Entry(window, show="*")
    n_conf_password_field_label = Label(window, text="Confirm Password")
    n_conf_password_field = Entry(window, show="*")

    n_register_button = Button(window, text="SUBMIT", command=register_function)

    # Place UI Elements to screen
    n_name_field_label.pack(pady=2)
    n_name_field.pack(pady=2)
    n_name_field.focus()
    n_username_field_label.pack(pady=2)
    n_username_field.pack(pady=2)
    n_password_field_label.pack(pady=2)
    n_password_field.pack(pady=2)
    n_conf_password_field_label.pack(pady=2)
    n_conf_password_field.pack(pady=2)
    n_register_button.pack(pady=1)

def dashboard(username):
    volunteer_data, stats_data, coin_data = db.load_databases()
    def refresh_dash():
        time.sleep(2)
        dashboard(username)
    def logout():
        date_now = datetime.now()
        dt_string = date_now.strftime("%d/%m/%Y | %H:%M:%S")
        users.update_volunteer(username=username, key="last_session", value=dt_string)
        db.save_database(db_name="total_stats", db_key="last_update", db_file=dt_string)
        coins.save_log_file()
        login_or_register()
    def verify_bag():
        try:
            selected_coin_type = coin_type_dropdown_variable.get()
            selected_coin_type = selected_coin_type.strip('p')
            selected_bag_weight = float(bag_weight_input.get())
            selected_bag_weight = int(selected_bag_weight * 100)
            add_remove, adjustment = coins.verify_bag(username=username, coin_type=selected_coin_type, bag_weight=selected_bag_weight)
            if (add_remove == "CORRECT"):
                verify_bag_title_label.config(text="Bag Verified", fg='green')
                refresh_dash()
            elif (add_remove == "ADD"):
                verify_bag_title_label.config(text=f'Please Add ({adjustment}) coin(s)')
                refresh_dash()
            else:
                verify_bag_title_label.config(text=f'Please Remove ({adjustment}) coin(s)')
                refresh_dash()
        except ValueError:
            verify_bag_title_label.config(text="Incorrect Input, please read the Docs.", fg='red')
            refresh_dash()


    for widget in window.winfo_children():
        widget.destroy()
    window.geometry('500x650')
    #Right Side of dashboard
    analytics_container = Frame(window)
    analytics_container.pack(side= RIGHT, padx=20)
    global_analytics = Frame(analytics_container)
    global_analytics.pack(side=TOP)
    volunteer_list = Frame(analytics_container)
    volunteer_list.pack(side=BOTTOM)

    #left side of dashboard
    controls_container = Frame(window)
    controls_container.pack(side=LEFT, padx=20)
    button_panel_container = Frame(controls_container)
    button_panel_container.pack(side= TOP)
    verify_bag_container = Frame(controls_container)
    verify_bag_container.pack(side= BOTTOM)
    verify_bag_upper = Frame(verify_bag_container)
    verify_bag_upper.pack(side= TOP)
    verify_bag_lower = Frame(verify_bag_container)
    verify_bag_lower.pack(side= BOTTOM)
    verify_bag_lower_upper = Frame(verify_bag_lower)
    verify_bag_lower_upper.pack(side=TOP)
    verify_bag_lower_lower = Frame(verify_bag_lower)
    verify_bag_lower_lower.pack(side=BOTTOM)

    #Button Panel
    refresh_dashboard_button = Button(
        button_panel_container, text="REFRESH DASHBOARD", command=refresh_dash)
    logout_button = Button(button_panel_container, text="LOGOUT", command=logout)
    refresh_dashboard_button.pack()
    logout_button.pack()

    #Verify Bag Data
    coin_types = []
    for key, value in coin_data['bag_values'].items():
        coin_types.append(f"{key}p")
    verify_bag_separator_label1 = Label(
        verify_bag_upper, text="----------------------------")
    verify_bag_title_label = Label(
        verify_bag_upper, text="VERIFY BAG WEIGHT")
    verify_bag_separator_label2 = Label(
        verify_bag_upper, text="----------------------------")
    coin_type_dropdown_label = Label(verify_bag_upper, text="Coin Type:")
    coin_type_dropdown_variable = StringVar(verify_bag_upper)
    coin_type_dropdown_variable.set(coin_types[0])
    coin_type_dropdown = OptionMenu(verify_bag_upper, coin_type_dropdown_variable, *coin_types)
    bag_weight_label = Label(verify_bag_lower_upper, text="Bag weight (g):")
    bag_weight_input = Entry(verify_bag_lower_upper)
    bag_weight_button = Button(verify_bag_lower_lower, text="VERIFY BAG", command=verify_bag)
    
    verify_bag_separator_label1.pack(pady= 3)
    verify_bag_title_label.pack(pady= 3)
    verify_bag_separator_label2.pack(pady= 3)
    coin_type_dropdown_label.pack(pady=1, side= LEFT)
    coin_type_dropdown.pack(pady=1, side= RIGHT)
    bag_weight_label.pack(pady=1, side= LEFT)
    bag_weight_input.pack(pady=1, side= RIGHT)
    bag_weight_button.pack(pady=7)

    ## Global Analytics
    total_separator_label = Label(
        global_analytics, text="----------------------------")
    total_accuracy_label = Label(
        global_analytics, text=f'Overall Accuracy: {stats_data["total_accuracy"]}%')
    total_bags_checked_label = Label(
        global_analytics, text=f'Total Checked: {stats_data["total_bags_checked"]}')
    total_correct_label = Label(
        global_analytics, text=f'Total Correct: {stats_data["total_correct"]}')
    total_incorrect_label = Label(
        global_analytics, text=f'Total Incorrect: {stats_data["total_bags_checked"] - stats_data["total_correct"]}')
    last_update_label = Label(global_analytics, text=f'Accurate as of: {stats_data["last_update"]}')
    total_separator_label.pack(pady=3)
    total_accuracy_label.pack(pady=1)
    total_bags_checked_label.pack(pady=1)
    total_correct_label.pack(pady=1)
    total_incorrect_label.pack(pady=1)
    last_update_label.pack(pady=1)
    for key, value in volunteer_data.items():
        separator_label = Label(
            volunteer_list, text="----------------------------")
        volunteer_name_label = Label(volunteer_list, text=f'Name: {value["name"]}')
        volunteer_accuracy_label = Label(volunteer_list, text=f'Accuracy: {value["accuracy"]}%')
        volunteer_total_checked_label = Label(volunteer_list, text=f'Bags Checked: {value["bags_checked"]}')
        volunteer_total_correct_label = Label(
            volunteer_list, text=f'Bags Correct: {value["bags_correct"]}')
        volunteer_total_incorrect_label = Label(
            volunteer_list, text=f'Bags Incorrect: {value["bags_checked"] - value["bags_correct"]}')
        volunteer_last_session_label = Label(volunteer_list, text=f'Last Session: {value["last_session"]}')

        separator_label.pack(pady=3)
        volunteer_name_label.pack(pady=1)
        volunteer_accuracy_label.pack(pady=1)
        volunteer_total_checked_label.pack(pady=1)
        volunteer_total_correct_label.pack(pady=1)
        volunteer_total_incorrect_label.pack(pady=1)
        volunteer_last_session_label.pack(pady=2)

login_or_register()

# Add a title to the window, set the inital window size and then place (kind of) in the centre of screen
window.title('Coin Counter')
window.eval('tk::PlaceWindow . center')

window.mainloop()

# TO DO - Main screen (verify bag, see analytics, log out -> save last session date/time)