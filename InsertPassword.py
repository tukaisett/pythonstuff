#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 22:15:12 2018

@author: tukai
"""

from Tkinter import *
 
window = Tk()
 
window.title("Welcome to LikeGeeks app")
 
window.geometry('350x200')
 
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=0)
 
txt = Entry(window,width=10)
 
txt.grid(column=1, row=0)
 
def clicked():
 
    res = "Welcome to " + txt.get()
 
    lbl.configure(text= res)
 
btn = Button(window, text="Click Me", command=clicked)
 
btn.grid(column=2, row=0)
 
window.mainloop()