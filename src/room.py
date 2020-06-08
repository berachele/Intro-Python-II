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
        for item in self.itemList:
            print(f"\nYou see a {item}\n")

    def add(self, itemName):
        self.itemList.append(itemName)
        return itemName

    def remove(self, itemName):
        self.itemList.remove(itemName)
        return itemName