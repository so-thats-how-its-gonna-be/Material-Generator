import random
import os
import tkinter as ttk
from tkinter import CENTER, NE, S, Canvas, Frame, Grid, PhotoImage, Tk, font
import util
from pathlib import Path

from PIL import Image, ImageTk, ImageTransform

def rch(ch):
    return random.choice(ch)

word_list = [
    ["o", "bre", "a", "lu", "har", "blu", "con", "rab", "alu", "zin", "ma", "ar", "po", "sa", "jo", "rho", "ena"], 
    ["b", "man", "n", "mon", "min", "len", "rom", "eg", "lo", "po"], 
    ["and", "s", "act", "san", "ad", "c", "atr"], 
    ["ium", "inite", "ite", "in", "on", "ony"]]

output = ""

combo = random.randint(0, 2)
if combo == 0:
    output = rch(word_list[0]) + rch(word_list[1]) + rch(word_list[2]) + rch(word_list[3])
elif combo == 1:
    output = rch(word_list[0]) + rch(word_list[1]) + rch(word_list[3])
elif combo == 2:
    output = rch(word_list[0]) + rch(word_list[2]) + rch(word_list[3])

print(output.capitalize())
print(combo)

matreferences = os.getcwd() + "/material-references/"

matimg = Image.open(matreferences + rch(os.listdir(matreferences))).copy().save('instance.png')
util.grayscalify('instance.png')

R = random.randint(-200, 200)
G = random.randint(-200, 200)
B = random.randint(-200, 200)
util.colorify('instance.png', R, G, B)

blockreferences = os.getcwd() + "/block-references/"

blockimg = Image.open(blockreferences + rch(os.listdir(blockreferences))).copy().save('block-instance.png')
util.grayscalify('block-instance.png')

util.colorify('block-instance.png', R/2, G/2, B/2)

root = Tk()
frm = Frame(root, padx=10, pady=10)

ttk.Label(frm, text=output.capitalize()).grid(column=1, row=0)
frmimg = ImageTk.PhotoImage(Image.open('instance.png').copy().resize([128, 128], 0))
can = Canvas(frm, width=500, height=500)
can.create_image(250, 250, image=frmimg, anchor=CENTER)
can.grid(column=1, row=1)

ttk.Label(frm, text=f"Block Of {output.capitalize()}").grid(column=1, row=2)
frmblimg = ImageTk.PhotoImage(Image.open('block-instance.png').copy().resize([128, 128], 0))
canbl = Canvas(frm, width=500, height=500)
canbl.create_image(250, 250, image=frmblimg, anchor=CENTER)
canbl.grid(column=1, row=3)

frm.grid()
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)
root.mainloop()
