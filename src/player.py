# Write a class to hold player information, e.g. what room they are currently in.


class Player:
    def __init__(self, currentRoom, move, pouch=[]):
        self.currentRoom = currentRoom
        self.move = move
        self.pouch = pouch
    
    def __str__(self):
        return f'{self.currentRoom}'
        
    def restrict(self):
        if hasattr(self.currentRoom, f'{self.move}_to'):
            self.currentRoom = getattr(self.currentRoom, f'{self.move}_to')
            print(self.currentRoom)
            print(self.currentRoom.description)
            self.currentRoom.showItems()
        else:
            print("\nError! You can't move in that direction. Try again. ")

    def grabItem(self, itemName):
        self.pouch.append(itemName)
        return f"Successfully added {itemName} to pouch!"

    def dropItem(self, itemName):
        self.pouch.remove(itemName)
        return f"You dropped {itemName} from pouch."