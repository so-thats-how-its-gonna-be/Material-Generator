from random import randint, choice
from tkinter import Image
from PIL import Image
import math

def rch(ch):
    return choice(ch)

def grayscalify(path: str):
    """Make an image grayscale.

    Args:
        path (str): Path of the file to grayscale.
    """
    Image.open(path).convert('LA').save(path)

def colorify(path: str, R: float, G: float, B: float):
    """Tint an image a color with RGB values.

    Args:
        path (str): Path of the file to tint.
        R (float): Red value of RGB.
        G (float): Green value of RGB.
        B (float): Blue value of RGB.
    """
    image = Image.open(path).convert('RGBA')
    output = []
    for pix in image.getdata():
        if pix[3] in list(range(1, 256)):
            output.append((pix[0] + math.floor(R), pix[1] + math.floor(G), pix[2] + math.floor(B)))
        else:
            output.append(pix)
    image.putdata(output)
    image.save(path)

def spin(path: str):
    """Randomly rotate an image with a chance to do nothing.

    Args:
        path (str): Path of the file to randomly rotate.
    """
    if(randint(0, 2)==0):
        return
    Image.open(path).transpose(randint(0, 4)).save(path)
