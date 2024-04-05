#import code
import sys
sys.path.append(r'C:\Users\ninao\Desktop\JUSTIN\NDE\Python Project') 
import time
from Main_game import Challenge_1_table

def decipher_code():
    """Decipher the given code."""
    
#if __name__ == "__main__":
      # Box presentation integrated into the introductory message
    print("As you enter the Troll's Lair, you see that a locked treasure chest sits on a table illuminated by a single candle.")
    print()
    time.sleep(1)
    print("A note lays to the side of the chest. Written on it is a series of letters and numbers: ")
    print(" Break the code to open the chest!")
    time.sleep(1)
    Challenge_1_table.present_text_in_box(Challenge_1_table.text)
    #print(decipher_code())
    print("Your goal is to decipher the following code to reveal the contents of the treasure chest! ")
    print('0305180205182119')
    user_answer = input("Enter your answer: ").lower()  # Convert the input to lowercase for case-insensitivity

    # Check if the user's answer is correct
    if user_answer == "cerberus":
        print("Congratulations! You have deciphered the code and unlocked the treasure chest!")
