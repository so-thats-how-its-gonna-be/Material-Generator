from tkinter import Image
from PIL import Image
from PIL import ImageFilter

def grayscalify(path):
    Image.open(path).convert('LA').save(path)

def colorify(path):
    Image.composite(Image.open(path).convert('RGBA'), Image.new('RGBA', Image.open(path).size, 'red'), Image.open(path).copy().convert('L').filter(ImageFilter.SHARPEN)).save(path)
