# Write a class to hold player information, e.g. what room they are currently in.


class Player:
    def __init__(self, room, move):
        self.room = room
        self.move = move
    
    def __str__(self):
        return f'{self.room}'
        
    