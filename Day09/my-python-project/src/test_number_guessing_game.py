import modular_doctest_number_guessing_game_6
import move_game_num
import process_digit_input
import process_non_digit_input
import initialize
import config


def test_number_guessing_game():
    """
    This function runs a series of tests on the number guessing game to ensure its functionality.
    
    >>> test_number_guessing_game()
    All tests passed!
    """
    # Test initialization
    game_num = initialize.initialize_game()
    assert isinstance(game_num, int), "Game number should be an integer."
    
    # Test digit input processing
    new_game_num = process_digit_input.digit_input_check(str(game_num), game_num, False)
    assert new_game_num != game_num, "Game number should change after a valid guess."
    
    # Test non-digit input processing
    new_game_num = process_non_digit_input.non_digit_input_check("n", game_num, False)
    assert new_game_num != game_num, "Game number should change after reset command."
    assert config.DEBUG_MODE_IS_ON is False, "Debug mode should be off after reset."
    assert config.MOVE_MODE_IS_ON is False, "Move mode should be off after reset."
    
    # Test move mode functionality
    move_mode_available = True
    new_game_num = process_non_digit_input.non_digit_input_check("m", game_num, move_mode_available)
    assert new_game_num == game_num, "Game number should not change if move mode is toggled without a guess."
    assert config.MOVE_MODE_IS_ON is True, "Move mode should be on after toggling."
    new_game_num = process_non_digit_input.non_digit_input_check("s", game_num, move_mode_available)
    assert new_game_num == game_num, "Game number should not change if move mode is toggled without a guess."
    new_game_num = process_non_digit_input.non_digit_input_check("help", game_num, move_mode_available)
    assert new_game_num == game_num, "Game number should not change if move mode is toggled without a guess."
    new_game_num = process_non_digit_input.non_digit_input_check("", game_num, move_mode_available)
    assert new_game_num == game_num, "Game number should not change if move mode is toggled without a guess."

