import os
import tkinter as ttk
from tkinter import CENTER, Canvas, Frame, Tk

from PIL import Image, ImageTk

import material
from material import BLOCK_REFERENCES_FOLDER

# * Python 3.11.0
# * Pillow 9.3.0

# How large the sprites will appear in the GUI
IMG_SIZE = [192, 192]

global root

def rerun():
    root.destroy()
    main()

def main():

    generated_material = material.Material.random()

    generated_material_block = material.MaterialBlock(generated_material, parent_sprite_path=material.MaterialBlock.random_sprite_alt(os.path.join(os.getcwd(
    ), BLOCK_REFERENCES_FOLDER, material.MaterialBlock.random_sprite()), generated_material.color, generated_material.name, directory='generated-blocks'))

    # Root window
    root = Tk()
    root.title('Material Generator')
    frame = Frame(root)

    # Material name
    ttk.Label(frame, text=generated_material.name.capitalize()).grid(column=0, row=0)
    frame_material_image = ImageTk.PhotoImage(
        Image.open(generated_material.parent_sprite).copy().resize(IMG_SIZE, 0))
    # Canvas containing the material sprite
    canvas_material = Canvas(frame, width=256, height=256)
    canvas_material.create_image(
        128, 128, image=frame_material_image, anchor=CENTER)
    canvas_material.grid(column=0, row=1)

    # Add separator between material and block
    ttk.Label(frame, text='\n\n').grid(column=0, row=2)

    # Name of block form
    ttk.Label(frame, text=generated_material_block.name.title()).grid(column=0, row=3)
    frame_block_image = ImageTk.PhotoImage(
        Image.open(generated_material_block.parent_sprite).copy().resize(IMG_SIZE, 0))
    # Canvas containing the block sprite
    canvas_block = Canvas(frame, width=IMG_SIZE[0]*4/3, height=IMG_SIZE[1]*4/3)
    canvas_block.create_image(
        IMG_SIZE[0]*2/3, IMG_SIZE[1]*2/3, image=frame_block_image, anchor=CENTER)
    canvas_block.grid(column=0, row=4)

    ttk.Button(frame, text="Regenerate", command=rerun).grid(column=0, row=87)
    ttk.Button(frame, text="Done", command=root.destroy).grid(column=0, row=88)
    frame.grid()
    root.mainloop()

main()