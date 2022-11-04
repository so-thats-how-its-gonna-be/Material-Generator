from random import choice as rch

class Material:
    def __init__(self, name: str, parentspritepath: str, color: tuple):
        self.name = name
        self.parentsprite = parentspritepath
        self.color = color
        
    def __str__(self):
        return f"""
{self.name}:
    - Parent Sprite Path: {self.parentsprite}
    - Color: {self.color}"""

class RawMaterial(Material):
    def __init__ (self, name: str, parentspritepath: str, color: tuple):
        super().__init__(name, parentspritepath, color)
        
    def __init__ (self, material: Material, name="Undefined", parentspritepath="Undefined", color="Undefined"):
        raw_name = name
        raw_color = color
        raw_parentspritepath = parentspritepath
        if raw_name == "Undefined": raw_name = f"Raw {material.name}"
        if raw_color == "Undefined": raw_color = material.color
        if raw_parentspritepath == "Undefined": raw_parentspritepath = material.parentsprite
        super().__init__(raw_name, raw_parentspritepath, raw_color)

class MaterialNugget(Material):
    def __init__ (self, name: str, parentspritepath: str, color: tuple):
        super().__init__(name, parentspritepath, color)
    
    def __init__ (self, material: Material, name="Undefined", parentspritepath="Undefined", color="Undefined"):
        nugget_name = name
        nugget_color = color
        nugget_parentspritepath = parentspritepath
        if nugget_name == "Undefined": nugget_name = f"{material.name} Nugget"
        if nugget_color == "Undefined": nugget_color = material.color
        if nugget_parentspritepath == "Undefined": nugget_parentspritepath = material.parentsprite
        super().__init__(nugget_name, nugget_parentspritepath, nugget_color)

class MaterialBlock(Material):
    def __init__ (self, name: str, parentspritepath: str, color: tuple):
        super().__init__(name, parentspritepath, color)
    
    def __init__ (self, material: Material, name="Undefined", parentspritepath="Undefined", color="Undefined"):
        block_name = name
        block_color = color
        block_parentspritepath = parentspritepath
        if block_name == "Undefined": block_name = rch([f"{material.name} Block", f"Block Of {material.name}"])
        if block_color == "Undefined": block_color = material.color
        if block_parentspritepath == "Undefined": block_parentspritepath = material.parentsprite
        super().__init__(block_name, block_parentspritepath, block_color)

# Unrefinable materials (like diamond or emerald)
# material -> material block
class Gem(Material):
    def __init__ (self, name: str, parentspritepath: str, color: tuple):
        super().__init__(name, parentspritepath, color)
        self.block = MaterialBlock(self)

# Refinable materials (like iron or gold)
# raw material -> material -> material block
# material nugget -> material -> material block
class Metal(Gem):
    def __init__ (self, name: str, parentspritepath: str, color: tuple):
        super().__init__(name, parentspritepath, color)
        self.nugget = MaterialNugget(self)
        self.raw = RawMaterial(self)

# Unrefinable misc materials (like lapis, coal, or redstone)
# material -> material block
class Mineral(Gem):
    def __init__ (self, name: str, parentspritepath: str, color: tuple):
        super().__init__(name, parentspritepath, color)
