class Material:
    def __init__(self, name, spritepath, blockpath, color):
        self.name = name
        self.spritepath = spritepath
        self.blockpath = blockpath
        self.color = color
        
    def __str__(self):
        return self.name
    
    def blockof(self):
        return "Block Of " + self.name
    
    def generatefull():
        return Material("test", "test", "test", "test")
    
    def lower(self):
        return self.name.lower()
