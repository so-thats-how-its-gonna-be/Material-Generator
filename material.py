from random import choice as rch

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

class MaterialRaw(Material):
    def __init__ (self, name: str, parent_sprite_path: str, color: tuple):
        super().__init__(name, parent_sprite_path, color)
        
    def __init__ (self, material: Material, name=None, parent_sprite_path=None, color=None):
        raw_name = name
        raw_color = color
        raw_parent_sprite_path = parent_sprite_path
        if raw_name == None: raw_name = f"Raw {material.name}"
        if raw_color == None: raw_color = material.color
        if raw_parent_sprite_path == None: raw_parent_sprite_path = material.parent_sprite
        super().__init__(raw_name, raw_parent_sprite_path, raw_color)

class MaterialNugget(Material):
    def __init__ (self, name: str, parent_sprite_path: str, color: tuple):
        super().__init__(name, parent_sprite_path, color)
    
    def __init__ (self, material: Material, name=None, parent_sprite_path=None, color=None):
        nugget_name = name
        nugget_color = color
        nugget_parent_sprite_path = parent_sprite_path
        if nugget_name == None: nugget_name = f"{material.name} Nugget"
        if nugget_color == None: nugget_color = material.color
        if nugget_parent_sprite_path == None: nugget_parent_sprite_path = material.parent_sprite
        super().__init__(nugget_name, nugget_parent_sprite_path, nugget_color)

class MaterialBlock(Material):
    def __init__ (self, name: str, parent_sprite_path: str, color: tuple):
        super().__init__(name, parent_sprite_path, color)
    
    def __init__ (self, material: Material, name=None, parent_sprite_path=None, color=None):
        block_name = name
        block_color = color
        block_parent_sprite_path = parent_sprite_path
        if block_name == None: block_name = rch([f"{material.name} Block", f"Block Of {material.name}"])
        if block_color == None: block_color = material.color
        if block_parent_sprite_path == None: block_parent_sprite_path = material.parent_sprite
        super().__init__(block_name, block_parent_sprite_path, block_color)

# Unrefinable materials (like diamond or emerald)
# material -> material block
class Gem(Material):
    def __init__ (self, name: str, parent_sprite_path: str, color: tuple):
        super().__init__(name, parent_sprite_path, color)
        self.block = MaterialBlock(self)

# Refinable materials (like iron or gold)
# raw material -> material -> material block
# material nugget -> material -> material block
class Metal(Gem):
    def __init__ (self, name: str, parent_sprite_path: str, color: tuple):
        super().__init__(name, parent_sprite_path, color)
        self.nugget = MaterialNugget(self)
        self.raw = MaterialRaw(self)

# Unrefinable misc materials (like lapis, coal, or redstone)
# material -> material block
class Mineral(Gem):
    def __init__ (self, name: str, parent_sprite_path: str, color: tuple):
        super().__init__(name, parent_sprite_path, color)
