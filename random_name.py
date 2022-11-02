from random import choice as rch, randint as rint
import os
import tkinter as ttk
from tkinter import CENTER, Canvas, Frame, Tk
from material import Material
import util

from PIL import Image, ImageTk


wordlist = [[], [], [], []]
for i, line in enumerate(open('wordlist.txt', 'r').readlines()):
    wordlist[i] = line.strip().split(' ')

matfile = 'material-instance.png'
blockfile = 'block-instance.png'

def main():
    
    matname = ''
    
    match rint(0, 2):
        case 0:
            matname = rch(wordlist[0]) + rch(wordlist[1]) + rch(wordlist[2]) + rch(wordlist[3])
        case 1:
            matname = rch(wordlist[0]) + rch(wordlist[1]) + rch(wordlist[3])
        case 2:
            matname = rch(wordlist[0]) + rch(wordlist[2]) + rch(wordlist[3])

    matname = matname.capitalize()

    matreferences = os.path.join(os.getcwd(), "material-references", "")

    Image.open(matreferences + rch(os.listdir(matreferences))).copy().save(matfile)
    util.grayscalify(matfile)

    RGB = (rint(-150, 150), rint(-150, 150), rint(-150, 150))
    util.tint(matfile, RGB)
    #Spin is disabled for now because the textures it generates are suboptimal.
    #util.spin(matfile)
    #Flip is disabled for now because the textures it generates have incorrect lighting.
    #util.flip(matfile, 0)

    blockreferences = os.path.join(os.getcwd(), "block-references", "")

    Image.open(blockreferences + rch(os.listdir(blockreferences))).copy().save(blockfile)
    util.grayscalify(blockfile)

    util.tint(blockfile, tuple([i / 2 for i in RGB]))

    root = Tk()
    frm = Frame(root, padx=10, pady=10)

    ttk.Label(frm, text=matname).grid(column=1, row=0)
    frmimg = ImageTk.PhotoImage(Image.open(matfile).copy().resize([128, 128], 0))
    can = Canvas(frm, width=500, height=500)
    can.create_image(250, 250, image=frmimg, anchor=CENTER)
    can.grid(column=1, row=1)

    ttk.Label(frm, text=f"Block Of {matname}").grid(column=1, row=2)
    frmblimg = ImageTk.PhotoImage(Image.open(blockfile).copy().resize([128, 128], 0))
    canbl = Canvas(frm, width=500, height=500)
    canbl.create_image(250, 250, image=frmblimg, anchor=CENTER)
    canbl.grid(column=1, row=3)

    frm.grid()
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)
    root.mainloop()

    testmat = Material(matname, matfile, RGB)
    print(testmat)
    print(testmat.blockof(blockfile))

main()
