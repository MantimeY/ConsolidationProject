 #importing modules I will need
import sys
import os
import csv
import random

# Function to  generate list of three random ints vetween 1 and 6, simulating the roll of three dice.
def roll_Dice():
    """
    Rolls three dice and retruns list of integers represention the outcome
	"""
    return	[random.randint(1,6) for _ in range(3)]

# Function to calculate the players score for a round 
def check_tuple_out(dice_roll):
    """
    checks to see if all three dice are the same
    return true if the player is tupled out, false if not
    """
    return dice_roll[0] == dice_roll[1] == dice_roll[2]

# Function to find which dice gets fixed
def get_fixed_dice(dice_roll):
    """
    Determines which dice are fixed (if two dice have the same value).
    returns a set of fixed values.
    """
    fixed_values = {val for val in dice_roll if dice_roll.count(val) > 1}
    return fixed_values 

# Function to simulate the player's turn
def play_Turn():
    """
    Simulates a single turn for a player, including dice rolling, rerolling, score keeping, etc.
    """
    # Initial roll
    dice = roll_Dice()
    print("You rolled: ", dice)


    # Check if the player "tuples out"
    if check_tuple_out(dice):
        print("Tuple out! You get 0 points this turn.")
        return 0
    
    # get the fixed dice
    fixed_dice = get_fixed_dice(dice)
    print("Fixed dice (cannot be rerolled):", fixed_dice)
    
    # Ask player if they want to reroll the non-fixed dice
    reroll_decision = input("Would you like to reroll the non-fixed dice? (yes or no): ").strip().lower()

    # keep rerolling until the player decides to stop or "tuple out"
    while reroll_decision == "yes":
        
        # reroll the non-fixed dice
        non_fixed_dice = [die for die in dice if die not in fixed_dice]
        
        for i in range(len(non_fixed_dice)):
            non_fixed_dice[i] = random.randint(1, 6)

        # update the dice with new rerolled values
        for i in range(len(dice)):
            if dice[i] not in fixed_dice:
                dice[i] = non_fixed_dice.pop(0)

        print("Your rolled: ", dice)

        # check if the player "tuples out" after the reroll
        if check_tuple_out(dice):
            print("Tuple out! You get 0 points this turn.")
            return 0

        # updated fixed dice
        fixed_dice = get_fixed_dice(dice)
        print("Fixed dice (cannot be rerolled):", fixed_dice)

        # Ask the player again if they want to reroll the non-fixed dice
        reroll_decision = input("Would you like to reroll the non-fixed dice? (yes or no): ").strip().lower()

    # If the player decides to stop, return the total score for the turn
    score = sum(dice)
    print("You decided to stop. Your score for this turn is:", score)
    return score

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

