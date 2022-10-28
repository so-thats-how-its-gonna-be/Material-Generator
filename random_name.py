import random
import os
import tkinter as tk
import util
from pathlib import Path

from PIL import Image

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

Image.open('instance.png').show(output)
