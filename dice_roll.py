import random

dice_roll = random.randint(1, 6)
decision = input('Do you want to play? ')


if decision.lower() == 'yes' or decision.lower() == 'y':
    print("Your number is- ")
    print(dice_roll)
else:
    print('''You did not enter a valid value.
    Or exited the game. 
    Enjoy your day!! ''')