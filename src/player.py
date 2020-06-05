# Write a class to hold player information, e.g. what room they are currently in.
from room import Room
from item import Item

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
            print("\nIf there are items in this room, you can 'get <itemname>' to add it to your pouch!\nYou can also 'drop <itemname> to remove it from your pouch.\n")
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


#TESTING
# player = Player(Room("outside", "asdfsdfklj", [Item("sword", "careful, it...Stings!")]), "none")

# print(player.pouch)

# player.grabItem("sword")

# print(player.pouch)

# player.dropItem("sword")

# print(player.pouch)