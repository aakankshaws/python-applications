# -*- coding: utf-8 -*-
"""
Create multi widget GUI (Practice)

Created on Thu Oct 11 11:20:03 2018

@author: M1039366
"""
from tkinter import *

window = Tk()

def converter():
    grams = float(e1_value.get()) * 1000
    t1.insert(END,grams)
    pounds = float(e1_value.get()) * 2.20462
    t2.insert(END,pounds)
    ounces = float(e1_value.get()) * 35.274
    t3.insert(END,ounces)    

t_kg =  Label(window, text='Kg')
t_kg.grid(row=0,column=0)

e1_value=StringVar()
e_kg = Entry(window,textvariable=e1_value)
e_kg.grid(row=0,column=1)

b_con = Button(window,text='Convert',command=converter)
b_con.grid(row=0,column=2)

t1 = Text(window,height=1,width=20)
t1.grid(row=1,column=0)

t2 = Text(window,height=1,width=20)
t2.grid(row=1,column=1)

t3 = Text(window,height=1,width=20)
t3.grid(row=1,column=2)

window.mainloop()
