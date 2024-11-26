 #importing modules I will need
import sys
import os
import csv
import random

# Function to  generate list of three random ints vetween 1 and 6, simulating the roll of three dice.
def roll_Dice():
    return	[random.randint(1,6) for _ in range(3)]

# Greets the player 
print ("Hello welcome to the game Tuple Out.")

# Ask the user if they would like to play
player_Choice = input("Would you like to play Tuple Out? (yes or no): ").strip().lower()


#intialize game variables
player_Score = 0
rounds = 0
max_Rounds = 5

# Responds based on the player's input
if player_Choice == "yes":
    print("great, Let's play")
    

elif player_Choice == "no":
    print("Okay we'll play another time")
else:
    print("Invalid response. Please type 'yes' or 'no'.")

