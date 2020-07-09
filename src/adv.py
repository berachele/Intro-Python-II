from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("sword", "slicer of death and cheese")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("diamond", "very shiny")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
player = Player(room['outside'], 'none')
print(player)
print(player.currentRoom.description)

print("\nUse your keyboard to command your character:\n   'n' goes North \n   'e' goes East\n   's' goes South\n   'w' goes West\n   and 'q' QUIT's the Game\nEnjoy your Adventure!\n")
quit_game = False

while not quit_game:
    player.move = input('I want to: ')
    action = player.move.split(" ")

    if len(action) == 2:
        print('HITTING THIS IF--LEN IS 2')
        if player.move == 'get ':
            player.grabItem({Item.itemName})
            player.currentRoom.itemList.remove({Item.itemName})
        else:
            player.dropItem({Item.itemName})
            player.currentRoom.itemList.add({Item.itemName})

    if player.move == 'q':
        print('Until next time, your adventure awaits!')
        quit_game = True

    else:
        player.restrict()

        #need to figure out how it recognizes what item you are wanting to pick up
        #go through array with items until it matches, then add to inventory
        #otherwise, drop in room