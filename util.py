from math import floor as fl
from random import randint as rint
from tkinter import Image

from PIL import Image

def grayscalify(path: str):
    """Make an image grayscale.

    Args:
        path (str): Path of the file to grayscale.
    """
    Image.open(path).convert('LA').save(path)

def tint(path: str, RGB: tuple):
    """Tint an image a color with RGB values. Floors RGB values to integers.

    Args:
        path (str): Path of the file to tint.
        RGB (tuple): RGB values to tint the image with.
    """
    image = Image.open(path).convert('RGBA')
    output = []
    for pix in image.getdata():
        #If the alpha value is 0, then the pixel is transparent, so we don't want to change it.
        if pix[3] in list(range(1, 256)):
            output.append((pix[0] + fl(RGB[0]), pix[1] + fl(RGB[1]), pix[2] + fl(RGB[2])))
        else:
            output.append(pix)
    image.putdata(output)
    image.save(path)

def spin(path: str, chance: int=3):
    """Randomly rotate an image with a chance to do nothing.

    Args:
        path (str): Path of the file to randomly rotate.
        chance (int, optional): Chance to do nothing, for example, a chance of 1 would cause this function to do nothing 50% of the time. Defaults to 3.
    """
    if rint(0, chance) == 0 and chance != 0:
        return
    Image.open(path).transpose(rint(2, 4)).save(path)

def flip(path: str, chance: int=3):
    """Randomly flip an image with a chance to do nothing.

    Args:
        path (str): Path of the file to randomly flip.
        chance (int, optional): Chance to do nothing, for example, a chance of 1 would cause this function to do nothing 50% of the time. Defaults to 3.
    """
    if rint(0, chance) == 0 and chance != 0:
        return
    Image.open(path).transpose(0).save(path)
