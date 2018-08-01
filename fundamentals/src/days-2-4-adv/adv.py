from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

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

# Create items
basketball = Item('basketball', 'a ball to play with')
book = Item('book', 'Extreme Ownership')
kettlebell = Item('kettlebell', 'to get ripped')

# Add items to rooms
room['outside'].add_item(basketball)
room['outside'].add_item(kettlebell)
room['foyer'].add_item(book)
room['overlook'].add_item(kettlebell)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

get_item = lambda item: item.name

def get_items(items):
    return ', '.join(list(map(get_item, items)))

def render_items(items):
    items = get_items(items)
    if items:
        print('\nItems: {}'.format(items))
    else:
        print('\nNo items added yet.\n')

def print_current_room_info(player):
    print('\nRoom Name: {}'.format(player.curr_room.name))
    print('Room Description: {}'.format(player.curr_room.description))
    render_items(player.curr_room.items)

def handle_direction_input(user_input, player):
    user_input += '_to'
    if hasattr(player.curr_room, user_input):
        player.curr_room = getattr(player.curr_room, user_input)
    else:
        print("\nNo room in this direction. Try again.\n")

def find_item(name, room):
    for item in room.items:
        if item.name == name:
            return item
    return None

is_playing = True
directions = ['n', 's', 'e', 'w']
inventory_commands = ['i', 'inventory']
get_commands = ['get', 'take']
drop_commands = ['drop']
invalid_command = "\nSorry, I didn't understand that. Please try again."

while is_playing:
    print_current_room_info(player)

    user_input = input('Go to a room: ')
    num_words = len(user_input.split())
    first_word = user_input.split()[0]

    if num_words == 1:
        if first_word in inventory_commands:
            render_items(player.items)
        else:
            print(invalid_command)
    elif num_words == 2:
        if first_word in get_commands:
            name = user_input.split()[1]
            item = find_item(name, player.curr_room)
            if item == None:
                print('\nThis room does not have that item. Try again.')
            else:
                player.curr_room.remove_item(item)
                player.add_item(item)
        elif first_word in drop_commands:
            name = user_input.split()[1]
            item = find_item(name, player)

            if item == None:
                print('\nThis player does not have that item. Try again.')
            else:
                player.remove_item(item)
                player.curr_room.add_item(item)
        else:
            print(invalid_command)


    else:
        print('Input must be one or two words. Please try again.')


    if user_input in directions:
        handle_direction_input(user_input, player)
    elif user_input == 'q':
        is_playing = False
