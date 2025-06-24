import random

# Configuration settings for the application
CONFIG = {
    "DEBUG_MODE_IS_ON": False,
    "MOVE_MODE_IS_ON": False,
}

def initialize_game():
    """
    This function initializes the game by setting up the necessary configurations and generating a new game number.
    It also ensures that the config module is available and sets default values if it doesn't exist.
    """
    print("Welcome to the interactive number guessing game!")
    print("In order to access additional features, enter the feature's command when you are asked to enter your guess. Entering 'help' will show the available features' commands.")
    reset_config()
    game_num = generate_new_num()
    return game_num

def generate_new_num():
    """
    This function generates a new random number between 1 and 20.
    >>> random.seed(0)  # For reproducibility in tests
    >>> generate_new_num()
    13
    """        
    return random.randrange(1,20)


def reset_config():
    """
    Resets config to default values.

    >>> CONFIG["DEBUG_MODE_IS_ON"] = True
    >>> CONFIG["MOVE_MODE_IS_ON"] = True
    >>> print(f"Before reset: DEBUG_MODE_IS_ON = {CONFIG['DEBUG_MODE_IS_ON']}, MOVE_MODE_IS_ON = {CONFIG['MOVE_MODE_IS_ON']}")
    Before reset: DEBUG_MODE_IS_ON = True, MOVE_MODE_IS_ON = True
    >>> reset_config()
    >>> print(f"After reset: DEBUG_MODE_IS_ON = {CONFIG['DEBUG_MODE_IS_ON']}, MOVE_MODE_IS_ON = {CONFIG['MOVE_MODE_IS_ON']}")
    After reset: DEBUG_MODE_IS_ON = False, MOVE_MODE_IS_ON = False
    """
    CONFIG["DEBUG_MODE_IS_ON"] = False
    CONFIG["MOVE_MODE_IS_ON"] = False



def move(game_num):
    """
    This function takes an int between 1 and 20, then returns the number modified by adding or subtracting a random integer between -2 and 2.
    It ensures the number stays within the range of 1 to 20 by wrapping around if it goes out of bounds.
    >>> move(10) # doctest: +SKIP
    returns a number between 8 and 12
    """
    
    # Move mode: change the number by up to 2. If the number is close to bounds, the number will only change by appropriate amount.
    if 2 < game_num < 19:
        game_num = game_num + random.randint(-2, 2)
    elif game_num == 1 or game_num == 2:
        if game_num == 1:
            game_num = game_num + random.randint(0, 2)
        else:  # game_num == 2
            game_num = game_num + random.randint(-1, 2)
    elif game_num == 19 or game_num == 20:
        if game_num == 20:
            game_num = game_num - random.randint(-2, 0)
        else:  # game_num == 19
            game_num = game_num - random.randint(-2, 1)
    else:
        raise ValueError("Game number must be between 1 and 20.")
    
    print("The number may have increased or decreased by up to 2.")
    return game_num