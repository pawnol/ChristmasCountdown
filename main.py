'''
Christmas Countdown
Pawelski
11/14/2023
This program counts down the days, hours, minutes, and seconds
till Christmas day.
'''

import tkinter as tk
import datetime

def update_label():
    '''
    Updates the label with the time left.
    '''
    christmas = datetime.datetime(2023, 12, 25, 0, 0, 0)
    current_day = datetime.datetime.today()
    deltaT = christmas - current_day
    date_label.config(text="Till Christmas:\n" + str(deltaT))
    date_label.after(1000, update_label)

window = tk.Tk()
window.title("Christmas Countdown")
window.geometry("850x850")
window.iconbitmap("christmas_tree_icon.ico")

tree_source = tk.PhotoImage(file="christmas_tree_picture.png")
tree_label = tk.Label(window, image=tree_source)
tree_label.pack()

date_label = tk.Label(window, font=("Comic Sans MS", 48))
date_label.pack()

update_label()

window.mainloop()