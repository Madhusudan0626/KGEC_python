'''Write a program that generates a random number and asks the user to guess what the
number is. If the user's guess is higher than the random number, the program should
display "Too high, try again." If the user's guess is lower than the random number, the
program should display "Too low, try again." The program should use a loop that repeats
until the user correctly guesses the random number. Program should count and display
number of tries to win the game.'''

import random

computer = random.randint(1,100)
player = 0
tries=0

print("Guess My Number Game")

while(player != computer):
    player = int(input('Enter your guess: '))
    tries = tries + 1
	
    if player < computer:
        print('Too low, try again.')
    elif player > computer:
        print('Too high, try again.')
    else:
        print("Correct!,you got it in",tries,"tries")
