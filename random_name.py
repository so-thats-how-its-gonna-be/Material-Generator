import random
import tkinter as tk
import util

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

img = Image.new('RGB', (16, 16))

img.save("instance.png")

imgo = Image.open("instance.png")
imgo.show()

util.grayscalify('test.png')
util.colorify('test.png')
