import os
import tkinter as ttk
from random import choice as rch
from random import randint as rint
from tkinter import CENTER, Canvas, Frame, Tk

from PIL import Image, ImageTk

import material
import imgutils

#* Python 3.11.0 
#* Pillow 9.3.0

WORD_LIST = [line.strip().split(' ') for line in open('wordlist.txt', 'r').readlines()]

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
    
    #Define the material name
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
    imgutils.grayscalify(MATERIAL_FILE_PATH)
    imgutils.tint(MATERIAL_FILE_PATH, material_color)
    imgutils.spin(MATERIAL_FILE_PATH)
    imgutils.flip(MATERIAL_FILE_PATH)

    #Generate a block sprite
    Image.open(BLOCK_REFERENCES + rch(os.listdir(BLOCK_REFERENCES))).copy().save(BLOCK_FILE_PATH)
    imgutils.grayscalify(BLOCK_FILE_PATH)
    imgutils.tint(BLOCK_FILE_PATH, tuple([number / 2 for number in material_color]))
    imgutils.spin(BLOCK_FILE_PATH)
    imgutils.flip(BLOCK_FILE_PATH)

    #Root window
    root = Tk()
    root.title('Material Generator')
    frame = Frame(root)

    #Material name
    ttk.Label(frame, text=material_name).grid(column=0, row=0)
    frame_material_image = ImageTk.PhotoImage(Image.open(MATERIAL_FILE_PATH).copy().resize(IMG_SIZE, 0))
    #Canvas containing the material sprite
    canvas_material = Canvas(frame, width=256, height=256)
    canvas_material.create_image(128, 128, image=frame_material_image, anchor=CENTER)
    canvas_material.grid(column=0, row=1)

    #Add separator between material and block
    ttk.Label(frame, text='\n\n').grid(column=0, row=2)

    #Name of block form
    ttk.Label(frame, text=f"Block Of {material_name}").grid(column=0, row=3)
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
