from random import choice as rch, randint as rint
import os
import tkinter as ttk
from tkinter import CENTER, Canvas, Frame, Tk
from material import Material
import util

from PIL import Image, ImageTk

#TODO: Add more parts to the wordlist
wordlist = [[], [], [], []]
for i, line in enumerate(open('wordlist.txt', 'r').readlines()):
    wordlist[i] = line.strip().split(' ')

#Paths for instantiated sprites
matfile = 'material-instance.png'
blockfile = 'block-instance.png'

def main():
    
    #Reset the material name
    matname = ''
    
    #Generate a random name
    match rint(0, 2):
        case 0:
            #Part 1 + Part 2 + Part 3 + Part 4
            matname = rch(wordlist[0]) + rch(wordlist[1]) + rch(wordlist[2]) + rch(wordlist[3])
        case 1:
            #Part 1 + Part 2 + Part 4
            matname = rch(wordlist[0]) + rch(wordlist[1]) + rch(wordlist[3])
        case 2:
            #Part 1 + Part 3 + Part 4
            matname = rch(wordlist[0]) + rch(wordlist[2]) + rch(wordlist[3])

    #Make material name Title Case
    matname = matname.capitalize()

    #Reference paths for block and material sprites
    matreferences = os.path.join(os.getcwd(), "material-references", "")
    blockreferences = os.path.join(os.getcwd(), "block-references", "")

    #Color to be used for the material, in RGB format. These colors *should* be mild, but sometimes it generates a color that is too bright.
    RGB = (rint(-150, 150), rint(-150, 150), rint(-150, 150))

    #Generate a material sprite
    Image.open(matreferences + rch(os.listdir(matreferences))).copy().save(matfile)
    util.grayscalify(matfile)
    util.tint(matfile, RGB)
    #! Spin is disabled for now because the textures it generates are suboptimal.
    #util.spin(matfile)
    #! Flip is disabled for now because the textures it generates have incorrect lighting.
    #util.flip(matfile, 0)

    #Generate a block sprite
    Image.open(blockreferences + rch(os.listdir(blockreferences))).copy().save(blockfile)
    util.grayscalify(blockfile)
    util.tint(blockfile, tuple([i / 2 for i in RGB]))

    #Root window
    root = Tk()
    frm = Frame(root, padx=10, pady=10)

    #Material name
    ttk.Label(frm, text=matname).grid(column=1, row=0)
    frmimg = ImageTk.PhotoImage(Image.open(matfile).copy().resize([128, 128], 0))
    #Canvas containing the material sprite
    can = Canvas(frm, width=500, height=500)
    can.create_image(250, 250, image=frmimg, anchor=CENTER)
    can.grid(column=1, row=1)

    #Name of block form
    ttk.Label(frm, text=f"Block Of {matname}").grid(column=1, row=2)
    frmblimg = ImageTk.PhotoImage(Image.open(blockfile).copy().resize([128, 128], 0))
    #Canvas containing the block sprite
    canbl = Canvas(frm, width=500, height=500)
    canbl.create_image(250, 250, image=frmblimg, anchor=CENTER)
    canbl.grid(column=1, row=3)

    #Gridify the frame, add the "quit" button, and run the mainloop
    #FIXME: The quit button doesn't appear
    frm.grid()
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=5)
    root.mainloop()

    testmat = Material(matname, matfile, RGB)
    print(testmat)
    print(testmat.blockof(blockfile))

main()
