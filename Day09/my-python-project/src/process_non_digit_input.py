import config
import initialize
def non_digit_input_check(user_input: str, game_num: int, move_mode_available: bool):
    '''
    This function takes the user's input (string), the current game number (int), and a boolean indicating if move mode is available.
    It processes the input and performs actions based on the command given by the user.
    Either returns the (possibly updated) game number based on the command
    if the input is help it will show the available commands, if x it will exit the program,
    if s it will show the current number, if m it will toggle move mode,
    if d it will toggle debug mode, if n it will reset the game,
    if help it will show the available commands, and if the input is empty or irrelevant, it will restart the loop
    >>> try:
    ...     non_digit_input_check("x", 10, True)
    ... except SystemExit as e:
    ...     print(f'Exited with code {e.code}')
    Exited with code Thanks for playing!
    >>> non_digit_input_check("n", 10, True) # doctest: +SKIP
    The game is being reset.
    New game number generated (1-20)
    >>> non_digit_input_check("s", 10, True)
    The current number is: 10
    10
    >>> import config
    >>> config.MOVE_MODE_IS_ON = True
    >>> non_digit_input_check("m", 10, True)
    Move mode is now off. The number will not change anymore.
    10
    >>> config.MOVE_MODE_IS_ON
    False
    >>> non_digit_input_check("m", 10, True)
    Move mode is now on. The game's number might increase or decrease by up to 2 after each guess!
    10
    >>> config.MOVE_MODE_IS_ON
    True
    >>> non_digit_input_check("m", 10, False)
    Move mode is not available in this version of the game.
    10
    >>> config.DEBUG_MODE_IS_ON = False
    >>> non_digit_input_check("d", 10, True)
    Debug mode is now on.
    10
    >>> config.DEBUG_MODE_IS_ON
    True
    >>> non_digit_input_check("d", 10, True)
    Debug mode is now off.
    10
    >>> config.DEBUG_MODE_IS_ON
    False
    >>> non_digit_input_check("help", 10, True)
    Available commands:
    x - Exit the game
    n - Reset the game
    s - Show the current number
    m - Toggle move mode (changes the number by up to 2 after each guess)
    d - Toggle debug mode (if enabled, shows the current number before each guess)
    10
    >>> non_digit_input_check("invalid input", 10, True)
    invalid input
    10
    >>> non_digit_input_check("", 10, True)
    invalid input
    10
    '''
    
    user_input = user_input.lower().strip()
    
    if user_input == "help":
        print("Available commands:")
        print("x - Exit the game")
        print("n - Reset the game")
        print("s - Show the current number")
        print("m - Toggle move mode (changes the number by up to 2 after each guess)")
        print("d - Toggle debug mode (if enabled, shows the current number before each guess)")
    elif user_input == "x":
        exit ("Thanks for playing!")
    elif user_input == "n":
        print("The game is being reset.")
        game_num = initialize.initialize_game()
        return game_num
    elif user_input == "s":
        print("The current number is:", game_num)
    elif user_input == "m":
        if move_mode_available is False:
            print("Move mode is not available in this version of the game.")
        else:
            config.MOVE_MODE_IS_ON = not config.MOVE_MODE_IS_ON
            print("Move mode is now", "on. The game's number might increase or decrease by up to 2 after each guess!" if config.MOVE_MODE_IS_ON
            else "off. The number will not change anymore.")
    elif user_input == "d":
        config.DEBUG_MODE_IS_ON = not config.DEBUG_MODE_IS_ON
        print("Debug mode is now "+ ("on." if config.DEBUG_MODE_IS_ON else "off."))
    else:
        print("invalid input")
    
    return game_num  # This will restart the loop in the main game function

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    
    game_num = non_digit_input_check("n", 10, True)
    print("Game number provided: 10")
    print("Game number after processing input:", game_num)