from room import Room
from player import Player
from item import Item
# Declare all items

items = {
    "sword": Item("sword", "excellent steel blade"),
    "torch": Item("torch", "handheld light source"),
    "potion": Item("potion", "rejuvenating health potion"),
    "club": Item("club", "imposing iron mace"),
    "shield": Item("shield", "hardy wooden shield"),
    "apple": Item("apple", "delicious green apple"),
    "chest": Item("chest", "golden chest with unknown treasure inside"),
    "key": Item("key", "rusty iron key"),
}

# Declare all the rooms

room = {
    "outside":  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items["sword"], items['club']]),

    "foyer":    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items["torch"], items['shield']]),

    "overlook": Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in the distance, 
but there is no way across the chasm.""", [items["potion"], items["chest"]]),

    "narrow":   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items["sword"], items["apple"]]),

    "treasure": Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items["torch"], items["key"]]),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input('Please input player name: ')
player = Player(name, room.outside)

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

user_input = None

while user_input is not 'q':
    print(f"{player.name} enters \"{player.room.name}\"")
    print(f"{player.room.desc}")
    user_input = input(
        "Move (n, s, w, e) or Take Action (get/take/drop/inv): ")
    if user_input == 'n' and hasattr(room[player.room], 'n_to'):
        print(f"it worked: {user_input}")
        player.room = room[player.room].n_to
    elif user_input == 's' and hasattr(room[player.room], 's_to'):
        player.room = room[player.room].s_to
    elif user_input == 'e' and hasattr(room[player.room], 'e_to'):
        player.room = room[player.room].e_to
    elif user_input == 'w' and hasattr(room[player.room], 'w_to'):
        player.room = room[player.room].w_to
    else:
        print(f"Can't move in that direction.")
