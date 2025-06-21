import random

def move(game_num):
    """
    This function takes an int between 1 and 20, then returns the number modified by adding or subtracting a random integer between -2 and 2.
    It ensures the number stays within the range of 1 to 20 by wrapping around if it goes out of bounds.
    >>> move(10) # doctest: +SKIP
    returns a number between 8 and 12
    """
    
    # Move mode: change the number by up to 2
    game_num = game_num + random.randint(-2, 2)
    if game_num < 1:
        game_num += 4
    elif game_num > 20:
        game_num -= 4
    print("The number may have increased or decreased by up to 2.")
    return game_num


if __name__ == "__main__":
    # This block is for testing purposes only
    game_num = 10  # Example number for testing
    print("Initial game number:", game_num)
    print("Calling move function...")
    game_num = move(game_num)  # Call the move function to see the effect
    print("New game number after move:", game_num)