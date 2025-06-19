import config
import initialize
def non_digit_input_check(user__input: str, game_num: int, move_mode_available: bool):
    '''
    if the input is help it will show the available commands, if x it will exit the program,
    if s it will show the current number, if m it will toggle move mode,
    if d it will toggle debug mode, if n it will reset the game,
    if help it will show the available commands, and if the input is empty or irrelevant, it will restart the loop
    '''
    
    user__input = user__input.lower().strip()
    
    if user__input == "help":
        print("Available commands:")
        print("x - Exit the game")
        print("n - Reset the game")
        print("s - Show the current number")
        print("m - Toggle move mode (changes the number by up to 2 after each guess)")
        print("d - Toggle debug mode (if enabled, shows the current number before each guess)")
    elif user__input == "x":
        print("Thanks for playing!")
        exit (0)
    elif user__input == "n":
        print("The game is being reset.")
        game_num = initialize.initialize_game()
        return game_num
    elif user__input == "s":
        print("The current number is:", game_num)
    elif user__input == "m":
        if move_mode_available is False:
            print("Move mode is not available in this version of the game.")
        else:
            config.MOVE_MODE_IS_ON = not config.MOVE_MODE_IS_ON
            print("Move mode is now", "on. The game's number might increase or decrease by up to 2 after each guess!" if config.MOVE_MODE_IS_ON
            else "off. The number will not change anymore.")
    elif user__input == "d":
        config.DEBUG_MODE_IS_ON = not config.DEBUG_MODE_IS_ON
        print("Debug mode is now "+ ("on." if config.DEBUG_MODE_IS_ON else "off."))
    else:
        print("invalid input")
    
    return game_num  # This will restart the loop in the main game function