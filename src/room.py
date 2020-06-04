# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, itemList=[]):
        self.name = name
        self.description = description
        self.itemList = itemList
    
    def __str__(self):
        return f"\nYou are in the {self.name}"

    def showItems(self):
        print("\nIn this room you see:")
        for item in self.itemList:
            print(f"{item}\n")