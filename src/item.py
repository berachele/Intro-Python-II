class Item:
    def __init__(self, itemName, iDescription):
        self.itemName = itemName
        self.iDescription = iDescription
    
    def __str__(self):
        return f"{self.itemName}: {self.iDescription}"