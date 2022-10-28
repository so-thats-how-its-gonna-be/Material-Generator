from tkinter import Image
from PIL import Image
from PIL import ImageFilter
import random

def grayscalify(path):
    Image.open(path).convert('LA').save(path)

def colorify(path):
    image = Image.open(path).convert('RGBA')
    output = []
    R = random.randint(-200, 200)
    G = random.randint(-200, 200)
    B = random.randint(-200, 200)
    for pix in image.getdata():
        if pix[3] in list(range(1, 256)):
            output.append((pix[0] + R, pix[1] + G, pix[2] + B))
        else:
            output.append(pix)
    image.putdata(output)
    image.save(path)
