from tkinter import *
import services.coin_service as coins
import services.user_service as users

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
        print(return_value, username)

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
                login_or_register()
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

login_or_register()
# Add a title to the window, set the inital window size and then place (kind of) in the centre of screen
window.title('Coin Counter')
window.eval('tk::PlaceWindow . center')

window.mainloop()

# TO DO - Main screen (verify bag, see analytics, log out -> save last session date/time)