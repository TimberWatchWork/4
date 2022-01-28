from tkinter import *

def clicked(UI):
    res = "Привет {}".format(UI.txt.get())
    UI.lbl.configure(text=res)