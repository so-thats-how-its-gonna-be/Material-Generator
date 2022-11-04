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

# Unrefinable materials (like diamond or emerald)
# material -> material block
class Gem(Material):
    def __init__ (self, name: str, parentspritepath: str, color: tuple):
        super().__init__(name, parentspritepath, color)

# Refinable materials (like iron or gold)
# raw material -> material -> material block
# material nugget -> material -> material block
class Metal(Material):
    def __init__ (self, name: str, parentspritepath: str, color: tuple):
        super().__init__(name, parentspritepath, color)
class RawMetal(Material):
    def __init__ (self, name: str, parentspritepath: str, color: tuple):
        super().__init__(name, parentspritepath, color)
    def __init__ (self, metal: Metal, name="Undefined", parentspritepath="Undefined", color="Undefined"):
        raw_name = name
        raw_color = color
        raw_parentspritepath = parentspritepath
        if name == "Undefined":
            raw_name = f"Raw {metal.name}"
        if color == "Undefined":
            raw_color = metal.color
        if parentspritepath == "Undefined":
            raw_parentspritepath = metal.parentsprite
        super().__init__(raw_name, raw_parentspritepath, raw_color)

# Unrefinable misc materials (like lapis, coal, or redstone)
# material -> material block
class Mineral(Material):
    def __init__ (self, name: str, parentspritepath: str, color: tuple):
        super().__init__(name, parentspritepath, color)
