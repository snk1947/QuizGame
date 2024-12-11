import tkintermapview
from textholders import *
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

window = tkinter.Tk()
window.geometry("1920x1200+0+0")
window.minsize(1920, 1200)
window.resizable(False, False)
window.state("normal")
window.title("ROOT")
window.config(background="blue")

map_widget = tkintermapview.TkinterMapView(window, width=1000, height=1000, corner_radius=0)
map_widget.place(x=450, y=100)


def motion(event):
    global pos_x, pos_y
    pos_x = event.x_root
    pos_y = event.y_root

    inp_posskjerm = ttk.Label(window, font=("Ariel", 16, "bold"), text=(pos_x))

    inp_posskjerm.place(x=115, y=277)


window.bind("<Motion>", motion)

window.mainloop()