from cProfile import label
import sqlite3, hashlib
from tabnanny import check
from tkinter import *

#Database
with sqlite3.connect("password_vault.db") as db:
    cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS masterpassword(
    id INTEGER PRIMARY KEY
    password TEXT NOT NULL);
""")

#Initiate Window
window = Tk()

window.title("Password Vault")

def firstScreen():
    window.geometry("250x150")
    lbl = Label(window, text="Create Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window, text="Re-Enter Password")
    lbl1.pack()

    txt1 = Entry(window, width=20, show="*")
    txt1.pack()
    txt1.focus()

    lbl2 = Label(window)
    lbl2.pack()

    def savePassword():
        if txt.get() == txt1.get():
            hashedPassword = txt.get()

            insert_password = """INSERT INTO masterpassword(password)
            VALUES(?)"""
            cursor.execute(insert_password, [(hashedPassword)])
        else:
            lbl2.config(text="Passwords must match.")

    btn = Button(window, text="Save", command=savePassword)
    btn.pack(pady=10)

def loginScreen():
    window.geometry("250x100")
    lbl = Label(window, text="Enter Master Password")
    lbl.config(anchor=CENTER)
    lbl.pack()

    txt = Entry(window, width=20, show="*")
    txt.pack()
    txt.focus()

    lbl1 = Label(window)
    lbl1.pack()

    def getMasterPassword():
        checkHashedPassword = txt.get()
        cursor.execute("SELECT * FROM masterpassword WHERE id = 1 AND password = ?", [(checkHashedPassword)])

    def checkPassword():
        password = "test"
        if password == txt.get():
            passwordVault()
        else:
            txt.delete(0, 'end')
            lbl1.config(text="Wrong Password.")

    btn = Button(window, text="Submit", command=checkPassword)
    btn.pack(pady=10)

def passwordVault():
    for widget in window.winfo_children():
        widget.destroy()
    window.geometry("700x350")

    lbl = Label(window, text="Password Vault")
    lbl.config(anchor=CENTER)
    lbl.pack()

firstScreen()
window.mainloop()