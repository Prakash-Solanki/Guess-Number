# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 21:12:52 2019

@author: solan
"""
import random
print('Hello! What is your name?')
myName = input()
Games = ' '
while Games ==' ':
    try:
        Games = int(input("How many games would you like to play?"))
    except:
        print("Please select a number")
for game in range(0,Games):
    pick = random.randint(1,25)
    guess = None
    Attempts = 0
    
    while pick !=guess:
        try:
            guess = int(input("Pick a number:"))
        except:
            print("Please select a number")
            continue
            
        if guess != pick:
            Attempts += 1
            if guess >pick:
                print("Your guess is too High!")
            else:
                print("Your guess is too Low!")
        else:
            print("Correct! It took you this much guess: %s"% Attempts)