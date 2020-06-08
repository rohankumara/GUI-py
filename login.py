# -*- coding: utf-8 -*-
"""
Created on: 8/06/2020

@author: Rohan Kumara
"""



from tkinter import *
import tkinter


def loginPage():
    login_screen=Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")

    Label(login_screen, text="Please enter login details").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username").pack()

    username_login_entry = Entry(login_screen,textvariable="username")
    username_login_entry.pack()

    Label(login_screen, text="")
    Label(login_screen, text="password").pack()
    
    password_login_entry = Entry(login_screen, textvariable="password", show = '*')
    password_login_entry.pack()

    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1 ).pack()
    login_screen.mainloop()

loginPage()
