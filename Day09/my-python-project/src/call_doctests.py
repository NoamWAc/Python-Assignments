import doctest
import base_functions
import modular_doctest_number_guessing_game_6 as game
import process_input

doctest.testmod(base_functions, verbose=True)
doctest.testmod(process_input, verbose=True)
doctest.testmod(game, verbose=True)

"""
    This function is for testing purposes only.
    >>> process_input.non_digit_input_check("help", 11, False) # This should show the help message
    11
    >>> process_input.non_digit_input_check("n", 11, False) # This should reset the game
    11
    >>> process_input.non_digit_input_check("s", 11, False) # This should show the current number
    11
    >>> game_num = process_input.non_digit_input_check("m", 11, False) # This should toggle move mode
    11
    >>> game_num = process_input.non_digit_input_check("d", 11, False) # This should toggle debug mode
    11
    >>> game_num = process_input.non_digit_input_check("invalid input", 11, False) # This should restart the loop
    11
    >>> game_num = process_input.non_digit_input_check("", 11, False) # This should restart the loop
    11
    >>> game_num = process_input.non_digit_input_check(123, 11, False) # This should raise a TypeError
    11
    >>> game_num = process_input.non_digit_input_check("x", 11, False) # This should exit the program
    11
    """