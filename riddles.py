# riddles.py

riddles = {
    "What dog keeps the best time?": "a watchdog"
    }
outcomes = { 
    'correct': "Congratulations! You have solved the riddle and unlocked the gates",
    'incorrect': "The stone dogs suddenly come to life and attack you. You try to fight them off but are quickly overwhelmed by their brute strength."
    }

def solve_riddle():
    print("solve_riddle")
    while True:
        print(f"To unlock the gate, you must solve the following riddle: \n ")
        print()
        answer = input("Your answer: ").lower()
        if answer == riddles["What dog keeps the best time?"]:
            print(outcomes['correct'])
            return True
        else:
            print(outcomes['incorrect'])
solve_riddle()