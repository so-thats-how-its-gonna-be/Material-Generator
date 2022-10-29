from tkinter import Image
from PIL import Image
from PIL import ImageFilter
import math
import random

def grayscalify(path):
    Image.open(path).convert('LA').save(path)

def colorify(path, R, G, B):
    image = Image.open(path).convert('RGBA')
    output = []
    for pix in image.getdata():
        if pix[3] in list(range(1, 256)):
            output.append((pix[0] + math.floor(R), pix[1] + math.floor(G), pix[2] + math.floor(B)))
        else:
            output.append(pix)
    image.putdata(output)
    #image = image.transpose(random.randint(0, 4))
    image.save(path)
