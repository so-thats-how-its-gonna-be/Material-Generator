import os
import tkinter as ttk
from random import choice as rch
from random import randint as rint
from tkinter import CENTER, Canvas, Frame, Tk

from PIL import Image, ImageTk

import imgutils
import material

#* Python 3.11.0
#* Pillow 9.3.0

#Paths for instantiated sprites
MATERIAL_FILE_PATH = 'material-instance.png'
BLOCK_FILE_PATH = 'block-instance.png'

MATERIAL_REFERENCES_FOLDER = 'material-references'
BLOCK_REFERENCES_FOLDER = 'block-references'

#Reference paths for block and material sprites
#Joins together the current directory, the desired reference folder, and then appends a blank string to the end of the path (resulting in a path that ends with a slash)
MATERIAL_REFERENCES = os.path.join(os.getcwd(), MATERIAL_REFERENCES_FOLDER, '')
BLOCK_REFERENCES = os.path.join(os.getcwd(), BLOCK_REFERENCES_FOLDER, '')

#How large the sprites will appear in the GUI
IMG_SIZE = [192, 192]

def main():

    gm = material.Material.random()

    gb = material.MaterialBlock(gm)

    #Root window
    root = Tk()
    root.title('Material Generator')
    frame = Frame(root)

    #Material name
    ttk.Label(frame, text=gm.name.capitalize()).grid(column=0, row=0)
    frame_material_image = ImageTk.PhotoImage(Image.open(gm.parent_sprite).copy().resize(IMG_SIZE, 0))
    #Canvas containing the material sprite
    canvas_material = Canvas(frame, width=256, height=256)
    canvas_material.create_image(128, 128, image=frame_material_image, anchor=CENTER)
    canvas_material.grid(column=0, row=1)

    #Add separator between material and block
    ttk.Label(frame, text='\n\n').grid(column=0, row=2)

    #Name of block form
    ttk.Label(frame, text=f"Block Of {gm.name.capitalize()}").grid(column=0, row=3)
    frame_block_image = ImageTk.PhotoImage(Image.open(BLOCK_FILE_PATH).copy().resize(IMG_SIZE, 0))
    #Canvas containing the block sprite
    canvas_block = Canvas(frame, width=IMG_SIZE[0]*4/3, height=IMG_SIZE[1]*4/3)
    canvas_block.create_image(IMG_SIZE[0]*2/3, IMG_SIZE[1]*2/3, image=frame_block_image, anchor=CENTER)
    canvas_block.grid(column=0, row=4)

    ttk.Button(frame, text="Regenerate").grid(column=0, row=87)
    ttk.Button(frame, text="Done", command=root.destroy).grid(column=0, row=88)
    frame.grid()
    root.mainloop()

#* END OF MAIN

test = material.Metal("Iron", "nah", (0,0,0))
print(test)
print(material.MaterialRaw(test))

main()
