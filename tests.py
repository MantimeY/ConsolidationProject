

import random

# Function to roll dice
def roll_Dice():
    """
    Rolls three dice and returns a list of integers representing the outcome.
    """
    results = [random.randint(1, 6) for _ in range(3)]
    return results

# Function to check if all dice are the same (tuple out)
def check_tuple_out(dice_roll):
    """
    Checks if all three dice are the same.
    Returns True if the player is tupled out, False if not.
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

# Test functions
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

def test_check_tuple_out():
    print("Testing check_tuple_out function...")
    print("Checking with [1, 1, 1]:", check_tuple_out([1, 1, 1]))  # Expected: True
    print("Checking with [1, 2, 3]:", check_tuple_out([1, 2, 3]))  # Expected: False

def test_get_fixed_dice():
    print("Testing get_fixed_dice function...")
    print("get_fixed_dice([1, 1, 2]):", get_fixed_dice_dict([1, 1, 2]))  # Expected: {1: 2}
    print("get_fixed_dice([3, 4, 5]):", get_fixed_dice_dict([3, 4, 5]))  # Expected: {}
    print("get_fixed_dice([6, 6, 6]):", get_fixed_dice_dict([6, 6, 6]))  # Expected: {6: 3}
    print("get_fixed_dice([6, 6, 7]):", get_fixed_dice_dict([6, 6, 7]))  # Expected: {6: 2}

# Now run the test functions
test_roll_dice()
test_check_tuple_out()
test_get_fixed_dice()
