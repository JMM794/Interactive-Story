import time

def solve_easy_puzzle():
    """Solve the riddle to unlock the gate."""
    while True:
        print("To unlock the gate, you must solve the following riddle:")
        print ()
        print("What dog keeps the best time?")
        print()
        answer = input("Your answer: ")
        print()
        if answer.lower() == "a watchdog" or answer.lower() == "watchdog" or answer.lower() == "A Watchdog" or answer.lower() == "a watch dog" or answer.lower() == "A watch dog" or answer.lower() == "A Watch Dog":
            print("Congratulations! You have solved the riddle and unlocked the gate.")
            print()
            time.sleep (1)
            print("As you answer the riddle, the stone dogs magically come to life and join you as companions on your journey.")
            time.sleep (1)
            print()
            navigate_the_maze()
            print()
        else:
            print("The stone dogs suddenly come to life and attack you. You try to fight them off but are quickly overwhelmed by their brute strength. A swift attack by one of the hounds knocks you unconcous!")
            print()
            time.sleep (1)
            print("You awake at the trunk of the tree you fell asleep at.")
            print()
            time.sleep (1)
            print("Please try again! Tip: You observe the gaurd dogs standing 'watch' over the gate.")
            print()
            solve_easy_puzzle()

def display_intro():
    """Display introduction to the maze."""
    print("Welcome to the Traveler's Maze! An interactive text-based minigame to test your ability to solve riddles and more!")
    print()
    user_response = input("Type 'Start' to start the adventure!: ")
    if user_response.lower() == "Start" or "start":
        time.sleep (1)
    print()
    print("After resting under an oak tree after a long day of travel, you awake to find a mysterious gate has appeared before you. Two large stone hounds stand on either side of the gate, appearing to stand watch over the mysterous iron gates.")
    time.sleep (1)
    print()
    print("There is a wooden sign with a message encraved on it-")
    print()
    user_response = input("Type 'Read' to Read the Sign: ")
    print()
    if user_response.lower() == "read":
        time.sleep (1)
        print("'BEWARE: Only the brave can navigate the treacherous path and uncover the secrets that lie within.'")
    time.sleep (1)
    print()
    while True:
        user_response = input("Do you wish to proceed? (Type 'Yes' or 'No'): ")
        print()
        if user_response.lower() == 'yes':
            print("You try to open the gate but discover it is locked!")
            print()
            break
        elif user_response.lower() == 'no':
            print("The stone hounds suddenly come to life and attack you. You try to fight them off but are quickly overwhelmed by their brute strength. A swift attack by one of the hounds knocks you unconcous!")
            print()
            time.sleep (3)
            print("You awake at the trunk of the tree you fell asleep at.")
            print("Do not be a coward and face your fears!")
            print()
            time.sleep (2)
        else:
            print("Some decisions require specific answers. Please type 'yes' or 'no'.")
    time.sleep (1) 

def navigate_the_maze():
    """Navigate the Maze"""
    print("You step through the gates with your new companions, and find yourself at the center of what seems to be a long stone walled hallway.")
    print()
    time.sleep (1) 
    while True:
        user_response = input("You have a choice to go either Right or Left. What do you choose?: ") 
        if user_response.lower() == "right":
            print("You turn right and travel to the end of the hall.")
            time.sleep (1)
            print(".")
            time.sleep (1)
            print(".")
            time.sleep (1)
            print (".")
            time.sleep (2)
            print("Awe man! It is just a dead end!") 
            print()
            time.sleep (1)
            print("Reluctantly, you walk back to the entrance.")
            print(".")
            print(".")
            print(".")
            print()
            time.sleep (2)
        elif user_response.lower() == "left":
            print("You turn left and travel to the end of the hallway.")
            print()
            time.sleep (1)
            print("The hallway turns left deeper into the maze. You hear something coming from the end of the hall but cannot make out it through the darkness.")
            print ("..")
            time.sleep (1)
            print ("Thump")
            print ()
            time.sleep (1)
            print("..")
            print ()
            time.sleep (1)
            print ("Thump")
            print ()
            time.sleep (1)
            print("..")
            print ()
            time.sleep (1)
            print ("Thump")
            print ()
            print ("A few paces into the dark hallway, the noise gets louder.")
            while True:
                    user_response = input ("Do you want to continue? Yes or No: ")
                    if user_response.lower() == "yes":
                        print ("Walking deeper into the darkness the sound stops abrouptly and you hear a deep growl coming from your companion gaurd dogs.")
                        print ()
                        time.sleep (1)
                        print ("..")
                        time.sleep (1)
                        print ("..")
                        time.sleep (1)
                        print ("..")
                        print ()
                        print("A few paces further, you notice a wooden door with on your left. Your companion hounds are focused on the shadows ahead of you, where the threating sound was coming from.")
                        time.sleep (1)
                        print ()
                        print("Suddenly, the loud noises return but ... ")
                        time.sleep (1)
                        print ("!!")
                        time.sleep (1)
                        print ()
                        print("It is running towards you!")
                        print ()
                        time.sleep (1)
                        print ("!!")
                        time.sleep (1)
                        print ()
                        print ("A large ugly troll with green skin and covered in boils charges you from the shadows!")
                        print ()
                        while True: 
                            user_response = input ("Do you fight or flee? Type 'fight' or 'flee': ")
                            if user_response.lower() == "fight" or user_response.lower() == "Fight" or user_response.lower() == "FIGHT":
                                    print("Prepare to fight!")
                                    print("The stone head of one of your gaurd hounds slides out of the darkness. The other hound races out of the shadows, badly damaged.")
                        time.sleep (1)
                    elif user_response.lower() == "no":
                        print ("You turn around, only to find that the way back has been sealed by a stone wall that was not there before. There is no choice besides to move forward, now!") 
        else:
            print ("There is no turning around now. Summon your courage and choose a path!")

def main():
    """Main function to run Act 1."""
    display_intro()
    solve_easy_puzzle()
    navigate_the_maze() 
    # Code to handle player input and progression to the next act

if __name__ == "__main__":
    main()
