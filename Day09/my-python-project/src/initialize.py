import os
import rng_1_to_20
import reset_config

def initialize_game():
    """
    This function initializes the game by setting up the necessary configurations and generating a new game number.
    It also ensures that the config module is available and sets default values if it doesn't exist.
    >>> initialize_game() # doctest: +SKIP
    Returns a random number between 1 and 20
    """
    
    reset_config.reset_config() # Tries to reset config file debug mode and move mode to false. If the file doesn't exist, create a default one
    game_num = rng_1_to_20.generate_new_num()
    return game_num

if __name__ == "__main__":
    # This block is only executed when the script is run directly, not when imported as a module.
    import doctest
    doctest.testmod(verbose=True)
