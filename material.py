import os
from random import choice as rch
from random import randint as rint

from PIL import Image

import imgutils

WORD_LIST = [line.strip().split(' ')
             for line in open('wordlist.txt', 'r').readlines()]

# Paths for instantiated sprites
MATERIAL_FILE_PATH = 'material-instance.png'
BLOCK_FILE_PATH = 'block-instance.png'

MATERIAL_REFERENCES_FOLDER = 'material-references'
BLOCK_REFERENCES_FOLDER = 'block-references'

# Reference paths for block and material sprites
# Joins together the current directory, the desired reference folder, and then appends a blank string to the end of the path (resulting in a path that ends with a slash)
MATERIAL_REFERENCES = os.path.join(os.getcwd(), MATERIAL_REFERENCES_FOLDER, '')
BLOCK_REFERENCES = os.path.join(os.getcwd(), BLOCK_REFERENCES_FOLDER, '')


class Material:
    def __init__(self, name: str, parent_sprite_path: str, color: tuple):
        self.name = name
        self.parent_sprite = parent_sprite_path
        self.color = color

    def __str__(self):
        return f"""
{self.name}:
    - Parent Sprite Path: {self.parent_sprite}
    - Color: {self.color}"""

    def random_name():
        match rint(0, 2):
            case 0:
                # Part 1 + Part 2 + Part 3 + Part 4
                return rch(WORD_LIST[0]) + rch(WORD_LIST[1]) + rch(WORD_LIST[2]) + rch(WORD_LIST[3])
            case 1:
                # Part 1 + Part 2 + Part 4
                return rch(WORD_LIST[0]) + rch(WORD_LIST[1]) + rch(WORD_LIST[3])
            case 2:
                # Part 1 + Part 3 + Part 4
                return rch(WORD_LIST[0]) + rch(WORD_LIST[2]) + rch(WORD_LIST[3])

    def random_color():
        return (rint(-150, 150), rint(-150, 150), rint(-150, 150))

    def random_sprite():
        return rch(os.listdir(MATERIAL_REFERENCES))

    def random_sprite_alt(path, color, name, tint=True, spin=True, flip=True, directory='generated-materials'):

        new_path = os.path.join(os.getcwd(), directory, name + '.png')

        # Create the generated-materials folder if it doesn't exist
        if not os.path.exists(os.path.join(os.getcwd(), directory)):
            os.mkdir(os.path.join(os.getcwd(), directory))
        Image.open(path).copy().save(new_path)
        imgutils.grayscalify(new_path)
        if tint:
            imgutils.tint(new_path, color)
        if spin:
            imgutils.spin(new_path)
        if flip:
            imgutils.flip(new_path)

        return new_path

    def random():
        material_name = Material.random_name()
        material_color = Material.random_color()
        return Material(material_name, Material.random_sprite_alt(os.path.join(os.getcwd(), MATERIAL_REFERENCES_FOLDER, Material.random_sprite()), material_color, material_name), material_color)


class MaterialRaw(Material):
    def __init__(self, name: str, parent_sprite_path: str, color: tuple):
        super().__init__(name, parent_sprite_path, color)

    def __init__(self, material: Material, name=None, parent_sprite_path=None, color=None):
        raw_name = name
        raw_color = color
        raw_parent_sprite_path = parent_sprite_path
        if raw_name == None:
            raw_name = f"Raw {material.name}"
        if raw_color == None:
            raw_color = material.color
        if raw_parent_sprite_path == None:
            raw_parent_sprite_path = material.parent_sprite
        super().__init__(raw_name, raw_parent_sprite_path, raw_color)


class MaterialNugget(Material):
    def __init__(self, name: str, parent_sprite_path: str, color: tuple):
        super().__init__(name, parent_sprite_path, color)

    def __init__(self, material: Material, name=None, parent_sprite_path=None, color=None):
        nugget_name = name
        nugget_color = color
        nugget_parent_sprite_path = parent_sprite_path
        if nugget_name == None:
            nugget_name = f"{material.name} Nugget"
        if nugget_color == None:
            nugget_color = material.color
        if nugget_parent_sprite_path == None:
            nugget_parent_sprite_path = material.parent_sprite
        super().__init__(nugget_name, nugget_parent_sprite_path, nugget_color)


class MaterialBlock(Material):
    def __init__(self, name: str, parent_sprite_path: str, color: tuple):
        super().__init__(name, parent_sprite_path, color)

    def __init__(self, material: Material, name=None, parent_sprite_path=None, color=None):
        block_name = name
        block_color = color
        block_parent_sprite_path = parent_sprite_path
        if block_name == None:
            block_name = rch(
                [f"{material.name} Block", f"Block Of {material.name}", f"Compressed {material.name}"])
        if block_color == None:
            block_color = material.color
        if block_parent_sprite_path == None:
            block_parent_sprite_path = material.parent_sprite
        super().__init__(block_name, block_parent_sprite_path, block_color)

    def random_sprite():
        return rch(os.listdir(BLOCK_REFERENCES))

# Unrefinable materials (like diamond or emerald)
# material -> material block


class Gem(Material):
    def __init__(self, name: str, parent_sprite_path: str, color: tuple):
        super().__init__(name, parent_sprite_path, color)
        self.block = MaterialBlock(self)

# Refinable materials (like iron or gold)
# raw material -> material -> material block
# material nugget -> material -> material block


class Metal(Gem):
    def __init__(self, name: str, parent_sprite_path: str, color: tuple):
        super().__init__(name, parent_sprite_path, color)
        self.nugget = MaterialNugget(self)
        self.raw = MaterialRaw(self)

# Unrefinable misc materials (like lapis, coal, or redstone)
# material -> material block


class Mineral(Gem):
    def __init__(self, name: str, parent_sprite_path: str, color: tuple):
        super().__init__(name, parent_sprite_path, color)
