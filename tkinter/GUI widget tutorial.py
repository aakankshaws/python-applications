# -*- coding: utf-8 -*-
"""
Tutorial of GUI tkinter widget of 
converting kms to miles

Created on Wed Oct 10 18:16:27 2018

@author: M1039366
"""
from tkinter import *

window = Tk()

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END,miles)

b1=Button(window,text='Execute',command=km_to_miles)
#b1.pack()
b1.grid(row=0,column=0)

e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)

window.mainloop()