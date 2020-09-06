import random

no_ofDices = int(input('How many dices do you want me to roll? '))

decision = input('Do you want to play? ')

while decision == decision.lower() == 'yes' or decision.lower() == 'y':
    dice_roll = random.randint(1, 6 * no_ofDices)

    if decision.lower() == 'yes' or decision.lower() == 'y':
        print("Your number is- ")
        print(dice_roll)
    a = input('Do you want to play again? ')
    if a ==  'yes' or a == 'y':
        continue
    else:
        print('''You did not enter a valid value.
        Or exited the game. 
        Enjoy your day!! ''')
        break 
