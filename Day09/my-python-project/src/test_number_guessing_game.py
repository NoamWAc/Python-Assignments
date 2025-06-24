import modular_doctest_number_guessing_game_6
import base_functions
import process_input



def test_number_guessing_game():
    """
    This function runs a series of tests on the number guessing game to ensure its functionality.
    
    >>> test_number_guessing_game()
    All tests passed!
    """
    # Test initialization
    game_num = base_functions.initialize_game()
    assert isinstance(game_num, int), "Game number should be an integer."
    game_num = base_functions.initialize_game()
    print("Initial game number:", game_num)
    game_num = base_functions.move(game_num)
    print("New game number after move:", game_num)
    game_num = base_functions.generate_new_num()
    print("Newly generated game number:", game_num)

      
    # Test non-digit input processing
    new_game_num = process_input.non_digit_input_check("n", game_num)
    assert new_game_num != game_num, "Game number should change after reset command. Chance of one in 20 that a newly generated number will be the same."
    assert base_functions.CONFIG["DEBUG_MODE_IS_ON"] is False, "Debug mode should be off after reset."
    assert base_functions.CONFIG["MOVE_MODE_IS_ON"] is False, "Move mode should be off after reset."
    
    # Test move mode functionality
    new_game_num = process_input.non_digit_input_check("m", game_num)
    assert new_game_num == game_num, "Game number should not change if move mode is toggled without a guess."
    assert base_functions.CONFIG["MOVE_MODE_IS_ON"] is True, "Move mode should be on after toggling."
    new_game_num = process_input.non_digit_input_check("s", game_num)
    assert new_game_num == game_num, "Game number should not change if move mode is toggled without a guess."
    new_game_num = process_input.non_digit_input_check("help", game_num)
    assert new_game_num == game_num, "Game number should not change if move mode is toggled without a guess."
    new_game_num = process_input.non_digit_input_check("", game_num)
    assert new_game_num == game_num, "Game number should not change if move mode is toggled without a guess."

    # Test digit input processing when move mode is on
    base_functions.CONFIG["MOVE_MODE_IS_ON"] = True
    new_game_num = process_input.digit_input_check(str(game_num), game_num)
    assert new_game_num != game_num, "Game number should change after a valid guess. (Chance of 1 in 3 or 5 that a newly generated number will be the same.)"