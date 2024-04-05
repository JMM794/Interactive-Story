

import sys
sys.path.append(r'C:\Users\ninao\Desktop\JUSTIN\NDE\Python Project')
import time

from Main_game import Challenge_1
from Main_game.Challenge_1 import decipher_code

def slow_print(text, delay=0.05):
    """Print text gradually."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_room_messages(room_name):
    '''Return room-specific messages.'''
    messages = {
        'Entrance Hall': 'You can go right or left down the dark hall. ',
        'Dead End': 'Oh no! This path leads to a dead end! Go back now.',
        'The Dark Passage': 'As you make your way down the Dark Passage, you notice a narrow path on the right. Ahead of you, you see light coming from beneath a door. Do you choose to go right or go forward? ',
        #"Troll's Lair": "Challenge_1.decipher_code()",
        'Narrow Path': 'As you walk down the Narrow Path, you start to hear ghostly whispers ahead of you. The path gets so narrow that you are forced to turn sideways to slip through. Just as the path gets too narrow to navigate, a corridor opens up on your right. Do you go right or go back? ',
        'Corridor of Whispers': ' The Corridor of Whispers leads to a large and luxurous mysterious chamber do you go forward or retrace your steps?',
        'Chamber of Echoes': 'The quiet whipsers from earlier have all grown into a symphany of indistinguishable chatter that fill your head. There is exits on your left and right or you can go back. ',
        'Dead End 2': 'Oh, no! It is a dead end. You have to go back!',
        'Sealed Passage': ' You have to find the key and unlock the passage!',
        'Gaurded Door': 'Gaurded Door Challenge',
    }

    return messages.get(room_name, "No message available for this room.")


rooms = {
    'Entrance Hall': { 
        'right': 'Dead End',
        'left': 'The Dark Passage'
    },
    'Dead End': {
        'back': 'Entrance Hall'
    },
    'The Dark Passage': {
        'straight': "Troll's Lair",
        'right': 'Narrow Path',
        'back': 'Entrance Hall'
    },
    "Troll's Lair": {
        'Challenge 1': 'Challenge 1',
        'back': 'The Dark Passage' 
    },
    'Narrow Path': {
        'right': 'Corridor of Whispers',
        'back': 'The Dark Passage'
    },
    'Corridor of Whispers': {
        'Challenge 2': 'Challenge 2',
        'forward': 'Chamber of Echoes',
        'back': 'Narrow Path'
    },
    'Chamber of Echoes': {
        'right': 'Dead End 2',
        'left': 'Sealed Passage',
        'back': 'Corridor of Whispers'
    },
    'Dead End 2': {
        'back': 'Chamber of Echoes'
    },
    'Sealed Passage': {
        'straight': 'Gaurded Door',
        'back': 'Chamber of Echoes'
    },
    'Guarded Door': {
        'straight': 'Chamber of Secrets',
        'back': 'Sealed Passage'
    },
    'Treasure Trove': {
        'enter': 'Final Chamber',
        'back': 'Gaurded Door'
    },
}

currentRoom = 'Entrance Hall'

def showStatus(currentRoom):
    """Determine the current status of the player."""
    # Print the player's current location
    print()
    slow_print('---------------------------')
    print()
    time.sleep(0.5)
    #print('You have made it safely to ' + currentRoom)
    #print()
    time.sleep(1.5)
    #print('Available directions:', ', '.join(rooms[currentRoom].keys()))
    slow_print(display_room_messages(currentRoom))

visited_rooms = []

while currentRoom != 'Final Chamber':
    showStatus(currentRoom)
    choice = input('Choose wisely > ')
    move = choice.lower().split(' ', 1)

    if move [0] == 'go':
        if len(move) == 2 and move[1].lower() in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1].lower()]
            print('You have made it safely to', currentRoom)
        else:
            print("You can't go that way!")
    elif move[0] == 'back':
      
        if visited_rooms:
            currentRoom = visited_rooms.pop()
            print('You have moved back to', currentRoom)
        else:
            print("There are no rooms to go back to!")
    else:
        print("Invalid command!")
        
    if currentRoom == "Troll's Lair":
        accept_challenge = input("Do you accept the challenge? (yes/no): ").lower()
        if accept_challenge == "yes":
            print("works")
            #Challenge_1.decipher_code()
        else:    
            print('Final Room')
