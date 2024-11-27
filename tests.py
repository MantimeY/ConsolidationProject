import ConsolidationProject
import random

# Function to generate list of three random ints between 1 and 6, simulating the roll of three dice.
def roll_Dice():
    """                     
    Rolls three dice and returns a list of integers representing the outcome.
    """
    results = [random.randint(1, 6) for _ in range(3)]
    return results

# Function to calculate the player's score for a round 
def check_tuple_out(dice_roll):
    """
    Checks to see if all three dice are the same.
    Returns True if the player is tupled out, False if not.
    """
    result = dice_roll[0] == dice_roll[1] == dice_roll[2]
    return result

# Function to find which dice gets fixed
def get_fixed_dice(dice_roll):
    """
    Determines which dice are fixed (if two dice have the same value).
    returns a set of fixed values.
    """
    fixed_values = {val for val in dice_roll if dice_roll.count(val) > 1}
    return fixed_values   

 # Test roll_Dice function
def test_roll_dice():
    print("Testing roll_Dice function...")
    dice = roll_Dice()
    print(f"Dice rolled: {dice}")
    if len(dice) == 3:
        print("roll_Dice test passed: Returned 3 dice.")
    else:
        print("roll_Dice test failed: Did not return 3 dice.")
    
    for die in dice:
        if 1 <= die <= 6:
            print(f"Dice roll {die} is within the valid range (1-6).")
        else:
            print(f"Dice roll {die} is out of the valid range (1-6).")

# Test check_tuple_out function
def test_check_tuple_out():
    print("Testing check_tuple_out function...")
    print("Checking with [1, 1, 1]:", check_tuple_out([1, 1, 1]))  # Expected: True
    print("Checking with [1, 2, 3]:", check_tuple_out([1, 2, 3]))  # Expected: False

# Test get_fixed_dice function
def test_get_fixed_dice(dice_roll):
    print("Testing get_fixed_dice function...")
    # Testing with different inputs to check fixed dice logic
    result1 = get_fixed_dice([1, 1, 2])  # Expected: {1}
    print("get_fixed_dice([1, 1, 2]):", result1)  
    result2 = get_fixed_dice([3, 4, 5])  # Expected: set()
    print("get_fixed_dice([3, 4, 5]):", result2)  
    result3 = get_fixed_dice([6, 6, 6])  # Expected: {6}
    print("get_fixed_dice([6, 6, 6]):", result3)

# Run the tests
test_roll_dice()
test_check_tuple_out()
test_get_fixed_dice()
