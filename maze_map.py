# Map for the game. Testing and practicing python world building.

#!/usr/bin/python3

def showInstruction():
    """Show the game instructions when called"""
    #!print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
        go [direction]
        get [item]
    ''')

inventory = []

currentRoom = '1st corridor'

showInstruction()
# the player MUST type somethin in
# otherwise input will keep asking
move = ''
while move == '':
    move = input ('>')

def showStatus():
    """determine the current status of the player"""
# print the player's current location
print('---------------------------')
print('You are in the ' + currentRoom)

#print what the player is carrying
print('Inventory:', inventory)

rooms = {
    '1st corridor': { 
        'right': 'dead end 1',
        'left': 'intersection 1'},
    'intersection 1': {
        'straight': '2nd corridor'},
    '2nd corridor': {
        'straight': 'trolls lair',
        'right': 'intersection 2'},
    'intersection 2': {
        'right': '3rd corridor'},
    '3rd corridor': {
        'right': ' intersection 3'},
    'intersection 3':{
        'straight': 'intersection 4',},
    'intersection 4':{
        'left': 'challenge room',
        'right': '4th corridor'},
    '4th corridor': {
        'right': 'intersection 5'},
    'intersection 5': {
        'straight': '5th corridor',
        'right': 'dead end 2'},
    '5th corridor': {
        'left': 'intersection 6'},
    'intersection 6': {
        'left': 'locked door 1',
        'straight': 'locked door 2'},
    'locked door 1': {
        'left': 'dead end 3'},
    'locked door 2': {
        'straight': 'intersection 7'},
    'intersection 7': {
        'right': 'treasure room'},
    'treasure room': {'Final Room'}
    }

if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
if move [0] == 'go':
    if move [1] in rooms[currentRoom]:
        currentRoom = rooms[currentRoom][move[1]]
    else:
        print("You can/'t go that way!")
if move [0] == 'get' :
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        inventory.append(move[1]) 
        print (move[1] == ' got!')
    else: print("Can/'t get " + move [1] + '1') 
if 'item' in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
showStatus()