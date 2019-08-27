#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') #There is a nice greeting
colors = ['red','orange','yellow','green','blue','violet','purple'] #These are the colors involved
play_again = '' # the play again is for when you succeed or fail.
best_count = sys.maxsize            # the biggest number 
while (play_again != 'n' and play_again != 'no'): #If you type n or no, the game ends
    match_color = random.choice(colors) #The favorite color is random.
    count = 0 #This is the beginnig tick of the counter of attempts.
    color = '' #The code starts here for your response.
    while (color != match_color): #If you guess the assinged color the following happens.
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() #Allows for capitals and spaces
        count += 1 #Adds a tick to the counter
        if (color == match_color): #Guess the assigned color
            print('Correct!') #You win
        else: #If you dont win
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #You guessed wrong and it tells you how many times that you tried.
    print('\nYou guessed it in {0} tries!'.format(count)) #How many times you guessed
    if (count < best_count): #If it takes less tries than before, it tells you that you did better.
        print('This was your best guess so far!') #<-'
        best_count = count #if the best count is the same, nothing happens.
    play_again = input("\nWould you like to play again? ").lower().strip() #It asks if you want to play again and you say a color.
print('Thanks for playing!') # A polite goodbye.