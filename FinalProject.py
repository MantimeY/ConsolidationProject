 #importing modules I will need

import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import time


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

# Define data_analysis globally
data_analysis = []

# Function to simulate the player's turn
def play_Turn(data_analysis):
    """
    Simulates a single turn for a player, including dice rolling, rerolling, score keeping, etc.
    """
    # Initial roll
    dice = roll_Dice()
    print("You rolled: ", dice)

    # add the initial roll to the data analysis list
    data_analysis.extend(dice)

    # Check if the player "tuples out"
    if check_tuple_out(dice):
        print("Tuple out! You get 0 points this turn.")
        return 0, dice, data_analysis

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
        data_analysis.extend(non_fixed_dice)

        print("You rolled: ", dice)

        # Check if the player "tuples out" after the reroll
        if check_tuple_out(dice):
            print("Tuple out! You get 0 points this turn.")
            return 0, dice, data_analysis

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
    return score, dice, data_analysis

# start the game  

# Greets the player 
print ("Hello welcome to the game Tuple Out.")
# Ask the user if they would like to play
player_Choice = input("Would you like to play Tuple Out? (yes or no): ").strip().lower()

# Responds based on the player's input
if player_Choice == "yes":
    print("great, Let's play")
    
	# intialize game variables
	# tracks the data for analysis and visualization

    round_scores = []
    dice_rolls = []
    player_Score = 0
    rounds = 0
    max_Rounds = 5
    target_Score= 50
# play up to the max_rounds and check the score

    while rounds < max_Rounds:
        print("Round", rounds+1)
   
         # Simulate a turn and the scores for that round
        rounds_score, dice, data_analysis = play_Turn(data_analysis)
        player_Score += rounds_score
       
	    # stores the scores for each round
        round_scores.append(rounds_score)
       
	    #stores the dice rolled for each round
        dice_rolls.append(dice)
        print("Your Current score is: " + str(player_Score))
    
	    # check if player has reached a score of 50 or more
        if player_Score >= 50:
            print("Congratulations! You've won the game with a score of: " + str(player_Score))
            break
    
        rounds +=1
    
	# If max_rounds are reached, print the final score
    if rounds == max_Rounds: 
         print("Game over. Your final score is: " + str(player_Score))
         
     # Data analysis happens after the game loop
    roll_counts = {i: data_analysis.count(i) for i in range(1, 7)}  # Dice roll counts
    
	 # Round with the most and least score
    max_score_round = round_scores.index(max(round_scores)) + 1 
    min_score_round = round_scores.index(min(round_scores)) + 1

    # Play rounds
    for roll in dice_rolls:
    # Add initial dice roll to the data_analysis list
      data_analysis.extend(roll) 

     

    
      print("Data Analysis: Number of times each number was rolled:")
      print(roll_counts)
      print("Round with the most score: Round " + str(max_score_round ))
      print("Round with the least score: Round " + str(min_score_round ))
    
      # data visualization of the roll counts
    plt.figure(figsize=(10, 6))
    plt.bar(roll_counts.keys(), roll_counts.values(), color='blue')
    plt.title("Roll Frequency for Each Dice Value")
    plt.xlabel("Dice Value")
    plt.ylabel("Frequency")
    plt.show()
    
    time.sleep(2)
	
    # Data Visualization of scores for each round
    plt.figure(figsize=(10, 6))
    plt.bar(range(1, rounds + 1), round_scores, color='green')
    plt.title("Scores per Round")
    plt.xlabel("Round")
    plt.ylabel("Score")
    plt.show()
      
    # created dataframe to store and analyze the scores and rolles

    df = pd.DataFrame({
    'Round': list(range(1, len(round_scores) + 1)),
    'Score': round_scores,
    'Dice Rolls': dice_rolls
})
    print("Detailed data for Each Round:", df)

    mean_score = np.mean(round_scores)
    median_score = np.median(round_scores)
    std_dev_score = np.std(round_scores)

    print("Mean Score:" +str(mean_score))
    print("Median Score:" + str(median_score))
    print("Standard Deviation of Scores:" +str(std_dev_score))

    time.sleep(2)
    # Using Seaborn for a more advanced plot
    sns.boxplot(data=round_scores, color='lightblue')
    plt.title('Distribution of Scores Across Rounds')
    plt.xlabel('Rounds')
    plt.ylabel('Score')
    plt.show()
    
     #loop ends here (Comment is for me)   

elif player_Choice == "no":
    print("Okay, we'll play another time.")
else:
    print("Invalid response. Please type 'yes' or 'no'.")