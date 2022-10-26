from tkinter import Image
from PIL import Image

def grayscalify(path):
    return Image.open(path).convert('LA').save(path)
