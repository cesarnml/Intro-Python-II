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
                     "North of you, the cave mount beckons",
                     [items["sword"], items['club']]),

    "foyer":    Room("Foyer", """Dim light filters in from the south.\nDusty passages run north and east.""", [items["torch"], items['shield']]),

    "overlook": Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness.
Ahead to the north, a light flickers in the distance, 
but there is no way across the chasm.""", [items["potion"], items["chest"]]),

    "narrow":   Room("Narrow Passage", """The narrow passage bends here from west to north.
    The smell of gold permeates the air.""", [items["sword"], items["apple"]]),

    "treasure": Room("Treasure Chamber", """You've found the long-lost treasure chamber! 
    Sadly, it has already been completely emptied by earlier adventurers. 
    The only exit is to the south.""", [items["torch"], items["key"]]),
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

choice = None
moved = True

while choice != 'q':
    if (choice in ['n', 's', 'w', 'e', None] and moved):
        print("===============\n")
        print(f"{player.name} enters \"{player.room.name}\"")
        print(f"{player.room.desc}\n")

    player.room.print_items()

# Player input
    choice = input(
        "\nCheck Inventory (i/inv), Move (n, s, w, e) or Take Action (get/take/drop): ")
    choice_arr = choice.split(' ')
    choice_len = len(choice_arr)
# Movement and Player Inventory Logic (expects 1 argument)
    if choice_len == 1:
        if (choice in ['n', 'N']) and hasattr(player.room, 'n_to'):
            moved = True
            player.room = player.room.n_to
        elif (choice in ['s', 'S']) and hasattr(player.room, 's_to'):
            moved = True
            player.room = player.room.s_to
        elif (choice in ['e', 'E']) and hasattr(player.room, 'e_to'):
            moved = True
            player.room = player.room.e_to
        elif (choice in ['w', 'W']) and hasattr(player.room, 'w_to'):
            moved = True
            player.room = player.room.w_to
        elif choice == 'i' or choice == 'inv' or choice == 'inventory':
            moved = False
            player.check_inventory()
        else:
            moved = False
            print(
                f"\n!*****!\nYou can't move in that direction. Please select another action.\n!*****!\n")


# Player Action Logic (expects 2 arguments)
    if choice_len == 2:
        if choice_arr[0] in ['get', 'take']:
            if items[choice_arr[1]] in player.room.items:
                player.take_item(items[choice_arr[1]])
                print(f"{player.name} picks up a {choice_arr[1]}!")
            else:
                print(f"That item isn't available to pick up.")
        if choice_arr[0] == 'drop':
            print('trying to drop something')


# Light Source Logic
