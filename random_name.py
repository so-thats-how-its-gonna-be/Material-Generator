import random

def rch(ch):
    return random.choice(ch)

import tkinter as tk

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
