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
    
    def blockof(self, blocksprite: str):
        return MaterialBlock(f"Block Of {self.name}", blocksprite, self.color, self)

class MaterialBlock:
    def __init__(self, name: str, parentblockspritepath: str, color: tuple, parentmaterial: Material):
        self.name = name
        self.blocksprite = parentblockspritepath
        self.color = color
        self.parentmaterial = parentmaterial
    
    def __str__(self):
        return f"""
{self.name}:
    - Block Sprite Path: {self.blocksprite}
    - Color: {self.color}
    - Parent Material: {self.parentmaterial.name}"""
