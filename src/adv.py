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
name = input('Input player name: ')
player = Player(name, room["outside"])
print("\n===============")
print(f"Welcome, {player.name}!")
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
    print("===============\n")
    print(f"{player.name} enters \"{player.room.name}\"")
    print(f"{player.room.desc}\n")
    player.room.print_items()
    user_input = input(
        "\nMove (n, s, w, e) or Take Action (get/take/drop/inventory): ")

# Movement Logic
    if len(user_input.split(' ')) == 1:
        if (user_input == 'n' or user_input == 'N') and hasattr(player.room, 'n_to'):
            player.room = player.room.n_to
        elif (user_input == 's' or user_input == 'S') and hasattr(player.room, 's_to'):
            player.room = player.room.s_to
        elif (user_input == 'e' or user_input == 'E') and hasattr(player.room, 'e_to'):
            player.room = player.room.e_to
        elif (user_input == 'w' or user_input == "W") and hasattr(player.room, 'w_to'):
            player.room = player.room.w_to
        elif user_input == 'i' or user_input == 'inv' or user_input == 'inventory':
            player.check_inventory()
        else:
            print(f"Your can't move in that direction. Please select another action.")


# Item Logic


# Light Source Logic
