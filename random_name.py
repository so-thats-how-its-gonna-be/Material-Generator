from random import choice as rch, randint as rint
import os
import tkinter as ttk
from tkinter import CENTER, Canvas, Frame, Tk
from material import Material
import util

from PIL import Image, ImageTk

#TODO: Add more parts to the wordlist
WORD_LIST = [[], [], [], []]
for i, line in enumerate(open('wordlist.txt', 'r').readlines()):
    WORD_LIST[i] = line.strip().split(' ')

#Paths for instantiated sprites
MATERIAL_FILE_PATH = 'material-instance.png'
BLOCK_FILE_PATH = 'block-instance.png'

#Reference paths for block and material sprites
MATERIAL_REFERENCES = os.path.join(os.getcwd(), "material-references", "")
BLOCK_REFERENCES = os.path.join(os.getcwd(), "block-references", "")

def main():
    
    #Reset the material name
    material_name = ''
    
    #Generate a random name
    match rint(0, 2):
        case 0:
            #Part 1 + Part 2 + Part 3 + Part 4
            material_name = rch(WORD_LIST[0]) + rch(WORD_LIST[1]) + rch(WORD_LIST[2]) + rch(WORD_LIST[3])
        case 1:
            #Part 1 + Part 2 + Part 4
            material_name = rch(WORD_LIST[0]) + rch(WORD_LIST[1]) + rch(WORD_LIST[3])
        case 2:
            #Part 1 + Part 3 + Part 4
            material_name = rch(WORD_LIST[0]) + rch(WORD_LIST[2]) + rch(WORD_LIST[3])

    #Make material name Title Case
    material_name = material_name.capitalize()

    #Color to be used for the material, in RGB format. These colors *should* be mild, but sometimes it generates a color that is too bright.
    material_color = (rint(-150, 150), rint(-150, 150), rint(-150, 150))

    #Generate a material sprite
    Image.open(MATERIAL_REFERENCES + rch(os.listdir(MATERIAL_REFERENCES))).copy().save(MATERIAL_FILE_PATH)
    util.grayscalify(MATERIAL_FILE_PATH)
    util.tint(MATERIAL_FILE_PATH, material_color)
    #! Spin is disabled for now because the textures it generates are suboptimal.
    #util.spin(matfile)
    #! Flip is disabled for now because the textures it generates have incorrect lighting.
    #util.flip(matfile, 0)

    #Generate a block sprite
    Image.open(BLOCK_REFERENCES + rch(os.listdir(BLOCK_REFERENCES))).copy().save(BLOCK_FILE_PATH)
    util.grayscalify(BLOCK_FILE_PATH)
    util.tint(BLOCK_FILE_PATH, tuple([number / 2 for number in material_color]))

    #Root window
    root = Tk()
    frame = Frame(root, padx=10, pady=10)

    #Material name
    ttk.Label(frame, text=material_name).grid(column=1, row=0)
    frame_material_image = ImageTk.PhotoImage(Image.open(MATERIAL_FILE_PATH).copy().resize([128, 128], 0))
    #Canvas containing the material sprite
    canvas_material = Canvas(frame, width=500, height=500)
    canvas_material.create_image(250, 250, image=frame_material_image, anchor=CENTER)
    canvas_material.grid(column=1, row=1)

    #Name of block form
    ttk.Label(frame, text=f"Block Of {material_name}").grid(column=1, row=2)
    frame_block_image = ImageTk.PhotoImage(Image.open(BLOCK_FILE_PATH).copy().resize([128, 128], 0))
    #Canvas containing the block sprite
    canvas_block = Canvas(frame, width=500, height=500)
    canvas_block.create_image(250, 250, image=frame_block_image, anchor=CENTER)
    canvas_block.grid(column=1, row=3)

    #Gridify the frame, add the "quit" button, and run the mainloop
    #FIXME: The quit button doesn't appear
    frame.grid()
    ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=5)
    root.mainloop()
#i-END OF MAIN

main()
