# Write a class to hold player information, e.g. what room they are currently in.


class Player:
    def __init__(self, currentRoom, move):
        self.currentRoom = currentRoom
        self.move = move
    
    def __str__(self):
        return f'{self.currentRoom}'
        
    