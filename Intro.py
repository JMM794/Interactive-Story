#Intro

# Intro.py

#import time

def display_intro():
    """Display introduction to the maze."""
print('display intro')
print("Welcome to the Maze! An interactive text-based minigame to test your ability to solve riddles and more!")
print()
#time.sleep(1)
user_response = input("Type 'Start' to start the adventure!: ")
if user_response.lower() == "start":
    #time.sleep(1)
    print()
    print("After resting under an oak tree after a long day of travel, you awake to find a mysterious gate has appeared before you. Two large stone hounds stand on either side of the gate, appearing to stand watch over the mysterious iron gates.")
    #time.sleep(1)
    print()
    print("There is a wooden sign with a message encraved on it-")
    print()
#time.sleep(1)
user_response = input("Type 'Read' to Read the Sign: ")
print()
if user_response.lower() == "read":
    #time.sleep(1)
    print("'BEWARE: Only the brave can navigate the treacherous path and uncover the secrets that lie within.'")
#time.sleep(1)
print()
while True:
    user_response = input("Do you wish to proceed? (Type 'Yes' or 'No'): ")
    print()
    if user_response.lower() == 'yes':
        print("You try to open the gate but discover it is locked!")
        print()
        break
    elif user_response.lower() == 'no':
        print("The stone hounds suddenly come to life and attack you. You try to fight them off but are quickly overwhelmed by their brute strength. A swift attack by one of the hounds knocks you unconscious!")
        print()
        #time.sleep(3)
        print("You awake at the trunk of the tree you fell asleep at.")
        print("Do not be a coward and face your fears!")
        print()
        #time.sleep(2)
    else:
        print("Some decisions require specific answers. Please type 'yes' or 'no'.")
#time.sleep(1)
