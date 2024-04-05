# Map for the game. Testing and practicing python world building.

#!/usr/bin/python3

#def slow_print 

print('script is running')
import time
from Main_game import Instructions
from Main_game import Intro
from Main_game import riddles
from Main_game import rooms
from Main_game import Challenge_1



def main():
    Instructions.showInstruction()
    Intro.display_intro()
    riddles.solve_riddle()
    currentRoom = '1st corridor'
    rooms.showStatus(currentRoom)
    Challenge_1.decipher_code()
    
if __name__ == "__main__":
    main()

#Get user input
choice = input('> ') 

move = choice.lower().split(' ', 1)