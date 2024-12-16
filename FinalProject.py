 #importing modules I will need

import random

# Function to  generate list of three random ints vetween 1 and 6, simulating the roll of three dice.
def roll_Dice():
    """
    Rolls three dice and retruns list of integers represention the outcome
	"""
    results = [random.randint(1,6) for _ in range(3)]
    return results

# Function to calculate the players score for a round 
def check_tuple_out(dice_roll):
    """
    checks to see if all three dice are the same
    return true if the player is tupled out, false if not
    """
    result = dice_roll[0] == dice_roll[1] == dice_roll[2]
    return result

# Function to get fixed dice and their counts (using a dictionary)
def get_fixed_dice_dict(dice_roll):
    """
    Determines which dice are fixed (if two or more dice have the same value).
    Returns a dictionary with fixed dice values as keys and their counts as values.
    """
    fixed_dice_dict = {val: dice_roll.count(val) for val in set(dice_roll) if dice_roll.count(val) > 1}
    return fixed_dice_dict

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
    
    # Get the fixed dice as a dictionary
    fixed_dice_dict = get_fixed_dice_dict(dice)
    fixed_dice_tuple = tuple(fixed_dice_dict.keys())  # Convert keys to tuple for immutability
    print("Fixed dice (value and count):", fixed_dice_dict)
    print("Fixed dice (immutable tuple):", fixed_dice_tuple)

    # Ask player if they want to reroll the non-fixed dice
    reroll_decision = input("Would you like to reroll the non-fixed dice? (yes or no): ").strip().lower()

    # Keep rerolling until the player decides to stop or "tuple out"
    while reroll_decision == "yes":
        # Reroll the non-fixed dice
        non_fixed_dice = [die for die in dice if die not in fixed_dice_tuple]
        for i in range(len(non_fixed_dice)):
            non_fixed_dice[i] = random.randint(1, 6)

        # Update the dice with new rerolled values
        for i in range(len(dice)):
            if dice[i] not in fixed_dice_tuple:
                dice[i] = non_fixed_dice.pop(0)

        print("You rolled: ", dice)

        # Check if the player "tuples out" after the reroll
        if check_tuple_out(dice):
            print("Tuple out! You get 0 points this turn.")
            return 0

        # Update fixed dice
        fixed_dice_dict = get_fixed_dice_dict(dice)
        fixed_dice_tuple = tuple(fixed_dice_dict.keys())  # Convert keys to tuple for immutability
        print("Fixed dice (value and count):", fixed_dice_dict)
        print("Fixed dice (immutable tuple):", fixed_dice_tuple)

        # Ask the player again if they want to reroll the non-fixed dice
        reroll_decision = input("Would you like to reroll the non-fixed dice? (yes or no): ").strip().lower()

    # If the player decides to stop, return the total score for the turn
    score = sum(dice)
    print("You decided to stop. Your score for this turn is:", score)
    return score


# start the game  
# Greets the player 
print ("Hello welcome to the game Tuple Out.")
# Ask the user if they would like to play
player_Choice = input("Would you like to play Tuple Out? (yes or no): ").strip().lower()

# Responds based on the player's input
if player_Choice == "yes":
    print("great, Let's play")
    
	#intialize game variables
    player_Score = 0
    rounds = 0
    max_Rounds = 5
    target_Score= 50
# play up to the max_rounds and check the score

    while rounds < max_Rounds:
        print("Round" + str(rounds+1))
   
         # Simulate a turn and the scores for that round
        rounds_score = play_Turn()
        player_Score += rounds_score
        print("Your Current score is: " + str(player_Score))
    
	    # check if player has reached a score of 50 or more
        if player_Score >= 50:
            print("Congratulations! You've won the game with a score of: " + str(player_Score))
            break
    
        rounds +=1
    
	# If max_rounds are reached, print the final score
    if rounds == max_Rounds: 
         print("Game over. Your final score is: " + str(player_Score))
    
     #loop ends here (Comment is for me)   

elif player_Choice == "no":
    print("Okay we'll play another time")
else:
    print("Invalid response. Please type 'yes' or 'no'.")


