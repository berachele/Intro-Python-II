# Write a class to hold player information, e.g. what room they are currently in.


class Player:
    def __init__(self, currentRoom, move):
        self.currentRoom = currentRoom
        self.move = move
    
    def __str__(self):
        return f'{self.currentRoom}'
        
    def restrict(self):
        if hasattr(self.currentRoom, f'{self.move}_to'):
            self.currentRoom = getattr(self.currentRoom, f'{self.move}_to')
            print(self.currentRoom)
            print(self.currentRoom.description)
        else:
            print("Error! You can't move in that direction. Try again. ")