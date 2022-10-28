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

references = os.getcwd() + "/material-references/"

reference = rch(os.listdir(references))

img = Image.open(references + reference).copy()

img.save('instance.png')

util.grayscalify('instance.png')
util.colorify('instance.png')

root = Tk()
frm = Frame(root, padx=10, pady=10)
frmimg = ImageTk.PhotoImage(Image.open('instance.png').copy().resize([128, 128], 0))
can = Canvas(frm, width=500, height=500)
can.create_image(250, 250, image=frmimg, anchor=CENTER)
can.grid(column=1, row=1)
frm.grid()
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)
ttk.Label(frm, text=output.capitalize(), font=font.BOLD).grid(column=1, row=0)
root.mainloop()
