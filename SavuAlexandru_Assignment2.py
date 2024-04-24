from tkinter import *
from tkinter import messagebox
import mysql.connector
import os
import time

db = mysql.connector.connect(host = "localhost", port = "3306", user = "root", passwd = "1234", database = "userinfo")
mycur = db.cursor()

def error_destroy():
    err.destroy()

def succ_destroy():
    succ.destroy()
    reg.destroy()

def succdel_destroy():
    delete.destroy()
    succ.destroy()
    logg.destroy()

def root_succdel_destroy():
    delete.destroy()
    succ.destroy()

def root_faildel_destroy():
    delete.destroy()
    fail.destroy()

def error():
    global err
    err = Toplevel(reg)
    err.title("Error")
    err.geometry("200x100")
    Label(err, text = "All fields are required.", fg = "brown3", font = "bold").pack()
    Label(err, text = "").pack()
    Button(err, text = "Ok", bg = "grey", width = 8, height = 1, command = error_destroy).pack()

def error_duplicate():
    global err
    err = Toplevel(reg)
    err.title("Error")
    err.geometry("350x100")
    Label(err, text = "An account with that username exists already.", fg = "brown3", font = "bold").pack()
    Label(err, text = "").pack()
    Button(err, text = "Ok", bg = "grey", width = 8, height = 1, command = error_destroy).pack()

def success():
    global succ
    succ = Toplevel(reg)
    succ.title("Success")
    succ.geometry("200x100")
    Label(succ, text = "Registration successful!", fg = "medium sea green", font = "bold").pack()
    Label(succ, text = "").pack()
    Button(succ, text = "Ok", bg = "grey", width = 8, height = 1, command = succ_destroy).pack()

def success_delete():
    global succ
    succ = Toplevel(delete)
    succ.title("Deletion Success")
    succ.geometry("200x100")
    Label(succ, text = "Deletion successful!", fg = "medium sea green", font = "bold").pack()
    Label(succ, text = "").pack()
    Button(succ, text = "Ok", bg = "grey", width = 8, height = 1, command = succdel_destroy).pack()

def root_success_delete():
    global succ
    succ = Toplevel(delete)
    succ.title("Deletion Success")
    succ.geometry("200x100")
    Label(succ, text = "Deletion successful!", fg = "medium sea green", font = "bold").pack()
    Label(succ, text = "").pack()
    Button(succ, text = "Ok", bg = "grey", width = 8, height = 1, command = root_succdel_destroy).pack()

def root_failure_delete():
    global fail
    fail = Toplevel(delete)
    fail.title("Deletion Failure")
    fail.geometry("275x100")
    Label(fail, text = "").pack()
    Label(fail, text = "You cannot delete the root account.", fg = "brown3", font = "bold").pack()
    Label(fail, text = "").pack()
    Button(fail, text = "Ok", bg = "grey", width = 8, height = 1, command = root_faildel_destroy).pack()

def admin_failure_delete():
    global fail
    fail = Toplevel(delete)
    fail.title("Deletion Failure")
    fail.geometry("315x100")
    Label(fail, text = "").pack()
    Label(fail, text = "You cannot delete another admin account.", fg = "brown3", font = "bold").pack()
    Label(fail, text = "").pack()
    Button(fail, text = "Ok", bg = "grey", width = 8, height = 1, command = root_faildel_destroy).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    power_info = power
    if username_info == "":
        error()
    elif password_info == "":
        error()
    else:
        sql = "insert into login values(%s, %s, %s)"
        t = (username_info, password_info, power_info)
        mycur.execute(sql, t)
        db.commit()
        Label(reg, text = "").pack()
        time.sleep(0.50)
        success()

def duplicate_verify():
    user_verify = username.get()
    dup_verify = int
    dup_sql = "select exists(select user from userinfo.login where user = %s) as truth;"
    mycur.execute(dup_sql, [(user_verify)])
    dup_verify = mycur.fetchone()
    if dup_verify[0]:
        error_duplicate()
    else:
        register_user()

def registration():
    global reg
    reg = Toplevel(menu)
    reg.title("Registration Portal")
    reg.geometry("300x250")
    global username
    global username_test
    global password
    global power
    power = 1
    Label(reg, text = "Register an account", bg = "grey", fg = "black", font = "bold", width = 300).pack()
    username = StringVar()
    password = StringVar()
    Label(reg, text = "").pack()
    Label(reg, text = "Username:", font = "bold").pack()
    Entry(reg, textvariable = username).pack()
    username_test = username
    Label(reg, text = "").pack()
    Label(reg, text = "Password:", font = "bold").pack()
    Entry(reg, textvariable = password, show = "*").pack()
    Label(reg, text = "").pack()
    Button(reg, text = "Register", font = "bold", bg = "SteelBlue1", command = duplicate_verify).pack()

def admin_registration():
    global reg
    reg = Toplevel(menu)
    reg.title("Administration Registration Portal")
    reg.geometry("300x250")
    global username
    global password
    global power
    power = 2
    Label(reg, text = "Register an account", bg = "grey", fg = "black", font = "bold", width = 300).pack()
    username = StringVar()
    password = StringVar()
    Label(reg, text = "").pack()
    Label(reg, text = "Username:", font = "bold").pack()
    Entry(reg, textvariable = username).pack()
    Label(reg, text = "").pack()
    Label(reg, text = "Password:", font = "bold").pack()
    Entry(reg, textvariable = password, show = "*").pack()
    Label(reg, text = "").pack()
    Button(reg, text = "Register", font = "bold", bg = "SteelBlue1", command = duplicate_verify).pack()

def logg_destroy():
    logg.destroy()

def fail_destroy():
    fail.destroy()

def logged_user():
    global logg
    logg = Toplevel(menu)
    logg.title("Welcome!")
    logg.geometry("400x250")
    Label(logg, text = "").pack()
    Label(logg, text = "").pack()
    Label(logg, text = "Welcome, {}!".format(username_verify.get()), fg = "medium sea green", font = "bold").pack()
    Label(logg, text = "").pack()
    Label(logg, text = "You current permission level is: Normal user.", font = "bold").pack()
    Label(logg, text = "").pack()
    Button(logg, text = "Delete account", width = "12", font = "bold", bg = "brown3", command = delete_user).pack()
    Label(logg, text = "").pack()
    Button(logg, text = "Log out", bg = "brown3", width = 8, height = 1, command = logg_destroy).pack()
    Label(logg, text = "").pack()

def logged_admin():
    global logg
    logg = Toplevel(menu)
    logg.title("Welcome!")
    logg.geometry("400x300")
    Label(logg, text = "").pack()
    Label(logg, text = "").pack()
    Label(logg, text = "Welcome, {}!".format(username_verify.get()), fg = "medium sea green", font = "bold").pack()
    Label(logg, text = "").pack()
    Label(logg, text = "You current permission level is: Administrator.", font = "bold").pack()
    Label(logg, text = "").pack()
    Button(logg, text = "User Registration", height = "1", width = "15", bg = "SteelBlue1", font = "bold", command = registration).pack()
    Label(logg, text = "").pack()
    Button(logg, text = "Delete account", width = "12", font = "bold", bg = "brown3", command = admin_delete_user).pack()
    Label(logg, text = "").pack()
    Button(logg, text = "Log out", bg = "brown3", width = 8, height = 1, command = logg_destroy).pack()
    Label(logg, text = "").pack()

def logged_root():
    global logg
    logg = Toplevel(menu)
    logg.title("Welcome!")
    logg.geometry("400x350")
    Label(logg, text = "").pack()
    Label(logg, text = "").pack()
    Label(logg, text = "Welcome, {}!".format(username_verify.get()), fg = "medium sea green", font = "bold").pack()
    Label(logg, text = "").pack()
    Label(logg, text = "You current permission level is: Root.", font = "bold").pack()
    Label(logg, text = "").pack()
    Button(logg, text = "User Registration", height = "1", width = "15", bg = "SteelBlue1", font = "bold", command = registration).pack()
    Label(logg, text = "").pack()
    Button(logg, text = "Admin Registration", height = "1", width = "20", bg = "SteelBlue1", font = "bold", command = admin_registration).pack()
    Label(logg, text = "").pack()
    Button(logg, text = "Delete account", width = "12", font = "bold", bg = "brown3", command = root_delete_user).pack()
    Label(logg, text = "").pack()
    Button(logg, text = "Log out", bg = "brown3", width = 8, height = 1, command = logg_destroy).pack()
    Label(logg, text = "").pack()

def failed():
    global fail
    fail = Toplevel(menu)
    fail.title("Invalid information.")
    fail.geometry("350x115")
    Label(fail, text = "").pack()
    Label(fail, text = "Invalid credentials, please try again.", fg = "red", font = "bold").pack()
    Label(fail, text = "").pack()
    Button(fail, text = "Ok", bg = "brown3", width = 8, height = 1, command = fail_destroy).pack()

def root_delete_user():
    global delete
    delete = Toplevel(menu)
    delete.title("User Deletion")
    delete.geometry("425x200")
    Label(delete, text = "").pack()
    Label(delete, text = "Introduce the username of the account you wish to delete:", font = "bold").pack()
    Entry(delete, textvariable = username_verify).pack()
    Label(delete, text = "").pack()
    Label(delete, text = "").pack()
    Label(delete, text = "Are you sure you wish to delete this account?", fg = "brown3", font = "bold").pack()
    Label(delete, text = "").pack()
    Button(delete, text = "Delete account", width = "12", font = "bold", bg = "brown3", command = root_delete_action).pack()

def admin_delete_user():
    global delete
    delete = Toplevel(menu)
    delete.title("User Deletion")
    delete.geometry("425x200")
    Label(delete, text = "").pack()
    Label(delete, text = "Introduce the username of the account you wish to delete:", font = "bold").pack()
    Entry(delete, textvariable = username_verify).pack()
    Label(delete, text = "").pack()
    Label(delete, text = "").pack()
    Label(delete, text = "Are you sure you wish to delete this account?", fg = "brown3", font = "bold").pack()
    Label(delete, text = "").pack()
    Button(delete, text = "Delete account", width = "12", font = "bold", bg = "brown3", command = admin_delete_action).pack()

def delete_user():
    global delete
    delete = Toplevel(menu)
    delete.title("User Deletion")
    delete.geometry("350x200")
    Label(delete, text = "").pack()
    Label(delete, text = "").pack()
    Label(delete, text = "").pack()
    Label(delete, text = "Are you sure you wish to delete your account?", font = "bold").pack()
    Label(delete, text = "").pack()
    Button(delete, text = "Delete account", width = "12", font = "bold", bg = "brown3", command = delete_action).pack()

def root_delete_action():
    user_verify = username_verify.get()
    sql = "select user from login where user = %s"
    sql2 = "delete from login where user = %s limit 1"
    mycur.execute(sql, [(user_verify)])
    results = mycur.fetchall()
    if results:
        if user_verify == 'root':
            root_failure_delete()
        elif user_verify != 'root':
            for i in results:
                mycur.execute(sql2, [(user_verify)])
                db.commit()
                root_success_delete()
                break
            
    else:
        failed()

def admin_delete_action():
    pwr_verify = int
    user_verify = username_verify.get()
    sql = "select user from login where user = %s"
    sql2 = "select power from login where user = %s"
    sql3 = "delete from login where user = %s limit 1"
    mycur.execute(sql, [(user_verify)])
    results = mycur.fetchall()
    mycur.execute(sql2, [(user_verify)])
    pwr_verify = mycur.fetchone()
    if results:
        if user_verify == 'root':
            root_failure_delete()
        elif pwr_verify[0] == 2:
            admin_failure_delete()
        elif user_verify != 'root':
            for i in results:
                mycur.execute(sql3, [(user_verify)])
                db.commit()
                root_success_delete()
                break
            
    else:
        failed()

def delete_action():
    user_verify = username_verify.get()
    pass_verify = password_verify.get()
    sql = "select * from login where user = %s and password = %s"
    sql2 = "delete from login where user = %s and password = %s limit 1"
    mycur.execute(sql, [(user_verify), (pass_verify)])
    results = mycur.fetchall()
    if results:
        for i in results:
            mycur.execute(sql2, [(user_verify), (pass_verify)])
            db.commit()
            success_delete()
            break
    else:
        failed()

def login_verify():
    pwr_verify = int
    user_verify = username_verify.get()
    pass_verify = password_verify.get()
    sql = "select * from login where user = %s and password = %s"
    sql2 = "select power from login where user = %s and password = %s"
    mycur.execute(sql, [(user_verify), (pass_verify)])
    results = mycur.fetchall()
    mycur.execute(sql2, [(user_verify), (pass_verify)])
    pwr_verify = mycur.fetchone()
    if results:
        for i in results:
            if pwr_verify[0] == 1:
                logged_user()
                break
            elif pwr_verify[0] == 2:
                logged_admin()
                break
            elif pwr_verify[0] == 3:
                logged_root()
                break
    else:
        failed()



def main_screen():
    global menu
    menu = Tk()
    menu.title("DEV6003 Application test")
    menu.geometry("700x400")
    Label(menu, text = "DEV6003 Application test", font = "bold", bg = "grey", fg = "black", width = 500).pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    Label(menu, text = "").pack()
    Label(menu, text = "").pack()
    Label(menu, text = "").pack()
    Label(menu, text = "Username:", font = "bold").pack()
    Entry(menu, textvariable = username_verify).pack()
    Label(menu, text = "").pack()
    Label(menu, text = "Password:", font = "bold").pack()
    Entry(menu, textvariable = password_verify, show = "*").pack()
    Label(menu, text = "").pack()
    Label(menu, text = "").pack()
    Button(menu, text = "Log in", width = "8", font = "bold", bg = "SteelBlue1", command = login_verify).pack()
    Label(menu, text = "").pack()
    Button(menu, text = "Sign up for an account", height = "1", width = "25", bg = "SteelBlue1", font = "bold", command = registration).pack()
    Label(menu, text = "").pack()
    Label(menu, text = "Please log in to access your data.").pack()

main_screen()
menu.mainloop()