import random
import os
from re import match
import tkinter as ttk
from tkinter import CENTER, Canvas, Frame, Tk
from material import Material
import util

from PIL import Image, ImageTk

#TODO: more words :)
wordlist = [
    ["o", "bre", "a", "lu", "har", "blu", "con", "rab", "alu", "zin", "ma", "ar", "po", "sa", "jo", "rho", "ena", "pi"], 
    ["b", "man", "n", "mon", "min", "len", "rom", "eg", "lo", "po"], 
    ["and", "s", "act", "san", "ad", "c", "atr"], 
    ["ium", "inite", "ite", "in", "on", "ony", "ar", "en"]]

output = ""

combo = random.randint(0, 2)
if combo == 0:
    output = util.rch(wordlist[0]) + util.rch(wordlist[1]) + util.rch(wordlist[2]) + util.rch(wordlist[3])
elif combo == 1:
    output = util.rch(wordlist[0]) + util.rch(wordlist[1]) + util.rch(wordlist[3])
elif combo == 2:
    output = util.rch(wordlist[0]) + util.rch(wordlist[2]) + util.rch(wordlist[3])

output = output.capitalize()

matreferences = os.getcwd() + "/material-references/"

matimg = Image.open(matreferences + util.rch(os.listdir(matreferences))).copy().save('instance.png')
util.grayscalify('instance.png')

R = random.randint(-200, 200)
G = random.randint(-200, 200)
B = random.randint(-200, 200)
util.colorify('instance.png', R, G, B)
util.spin('instance.png')

blockreferences = os.getcwd() + "/block-references/"

blockimg = Image.open(blockreferences + util.rch(os.listdir(blockreferences))).copy().save('block-instance.png')
util.grayscalify('block-instance.png')

util.colorify('block-instance.png', R*0.5, G*0.5, B*0.5)

root = Tk()
frm = Frame(root, padx=10, pady=10)

ttk.Label(frm, text=output).grid(column=1, row=0)
frmimg = ImageTk.PhotoImage(Image.open('instance.png').copy().resize([128, 128], 0))
can = Canvas(frm, width=500, height=500)
can.create_image(250, 250, image=frmimg, anchor=CENTER)
can.grid(column=1, row=1)

ttk.Label(frm, text=f"Block Of {output}").grid(column=1, row=2)
frmblimg = ImageTk.PhotoImage(Image.open('block-instance.png').copy().resize([128, 128], 0))
canbl = Canvas(frm, width=500, height=500)
canbl.create_image(250, 250, image=frmblimg, anchor=CENTER)
canbl.grid(column=1, row=3)

frm.grid()
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=4)
root.mainloop()
