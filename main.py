'''
Christmas Countdown
Pawelski
11/14/2023
This program counts down the days, hours, minutes, and seconds
till Christmas day.
'''

import tkinter as tk
import datetime
import timedelta_util

def update_label():
    '''
    Updates the label with the time left.
    '''
    christmas = datetime.datetime(2023, 12, 25, 0, 0, 0)
    current_day = datetime.datetime.today()
    deltaT = christmas - current_day
    days = deltaT.days
    hours = timedelta_util.actual_hours(deltaT)
    minutes = timedelta_util.actual_minutes(deltaT)
    seconds = timedelta_util.actual_seconds(deltaT)
    date_label.config(text="There are "+ str(days) + " days, "
                      + str(hours) + " hours, "
                      + str(minutes) + " minutes, \nand "
                      + str(seconds) + " seconds till Christmas!")
    date_label.after(1000, update_label)

window = tk.Tk()
window.title("Christmas Countdown")
window.geometry("900x825")
window.iconbitmap("christmas_tree_icon.ico")

tree_source = tk.PhotoImage(file="christmas_tree_picture.png")
tree_label = tk.Label(window, image=tree_source)
tree_label.pack()

date_label = tk.Label(window, font=("Comic Sans MS", 32))
date_label.pack()

update_label()

window.mainloop()