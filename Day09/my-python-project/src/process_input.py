import base_functions

def non_digit_input_check(user_input: str, game_num: int):
    '''
    This function takes the user's input (string), the current game number (int), and a boolean indicating if move mode is available.
    It processes the input and performs actions based on the command given by the user.
    Either returns the (possibly updated) game number based on the command
    If the input is help it will show the available commands, if x it will exit the program,
    If s it will show the current number, if m it will toggle move mode,
    If d it will toggle debug mode, if n it will reset the game,
    If help it will show the available commands, and if the input is empty or irrelevant, it will restart the loop
    >>> try:
    ...     non_digit_input_check("x", 10)
    ... except SystemExit as e:
    ...     print(f'Exited with code {e.code}')
    Exited with code Thanks for playing!
    >>> non_digit_input_check("n", 10) # doctest: +SKIP
    The game is being reset...

    Welcome to the interactive number guessing game!
    In order to access additional features, enter the feature's command when you are asked to enter your guess. Entering 'help' will show the available features' commands.
    * New game number will be generated (1-20)
    >>> non_digit_input_check("s", 10)
    The current number is: 10
    10
    >>> import base_functions
    >>> base_functions.CONFIG["MOVE_MODE_IS_ON"] = True
    >>> non_digit_input_check("m", 10)
    Move mode is now off. The number will not change anymore.
    10
    >>> base_functions.CONFIG["MOVE_MODE_IS_ON"]
    False
    >>> non_digit_input_check("m", 10)
    Move mode is now on. The game's number might increase or decrease by up to 2 after each guess!
    10
    >>> base_functions.CONFIG["MOVE_MODE_IS_ON"]
    True
    >>> base_functions.CONFIG["DEBUG_MODE_IS_ON"] = False
    >>> non_digit_input_check("d", 10)
    Debug mode is now on.
    10
    >>> base_functions.CONFIG["DEBUG_MODE_IS_ON"]
    True
    >>> non_digit_input_check("d", 10)
    Debug mode is now off.
    10
    >>> base_functions.CONFIG["DEBUG_MODE_IS_ON"]
    False
    >>> non_digit_input_check("help", 10)
    Available commands:
    x - Exit the game
    n - Reset the game
    s - Show the current number
    m - Toggle move mode (If enabled, changes the number by up to 2 after each guess)
    d - Toggle debug mode (If enabled, shows the current number before each guess)
    10
    >>> non_digit_input_check("invalid input", 10)
    invalid input
    10
    >>> non_digit_input_check("", 10)
    invalid input
    10
    '''
    
    user_input = user_input.lower().strip()
    
    if user_input == "help":
        print("Available commands:")
        print("x - Exit the game")
        print("n - Reset the game")
        print("s - Show the current number")
        print("m - Toggle move mode (If enabled, changes the number by up to 2 after each guess)")
        print("d - Toggle debug mode (If enabled, shows the current number before each guess)")
    elif user_input == "x":
        exit ("Thanks for playing!")
    elif user_input == "n":
        print("The game is being reset... \n")
        game_num = base_functions.initialize_game()
        return game_num
    elif user_input == "s":
        print("The current number is:", game_num)
    elif user_input == "m":
        base_functions.CONFIG["MOVE_MODE_IS_ON"] = not base_functions.CONFIG["MOVE_MODE_IS_ON"]
        print("Move mode is now", "on. The game's number might increase or decrease by up to 2 after each guess!" if base_functions.MOVE_MODE_IS_ON
        else "off. The number will not change anymore.")
    elif user_input == "d":
        base_functions.CONFIG["DEBUG_MODE_IS_ON"] = not base_functions.CONFIG["DEBUG_MODE_IS_ON"]
        print("Debug mode is now "+ ("on." if base_functions.CONFIG["DEBUG_MODE_IS_ON"] else "off."))
    else:
        print("invalid input")
    
    return game_num  # This will restart the loop in the main game function

def test(non_digit_input_check):
    game_num = non_digit_input_check("n", 10)
    print("Game number provided: 10")
    print("Game number after processing input:", game_num)


def digit_input_check(guessed_num, game_num):
    """
    This function takes user's guessed number, the game number, and a boolean indicating if move mode is available.
    It returns the (possibly updated) game number based on the user's guess.

    >>> digit_input_check(5, 10)
    Your guess was too low. Give it another try!
    10
    >>> digit_input_check(15, 10)
    Your guess was too high. Give it another try!
    10
    >>> digit_input_check(25, 10)
    Please only enter a number between 1 and 20!
    10
    
    
    """
    
    # if the input isn't an int, it will convert it to an integer and check if it is correct       
    if guessed_num != int:
        guessed_num = int(guessed_num)
    # if the guess is correct, it will inform the user and then ask them if to continue
    # if answer is "yes", reset number, if they answer otherwise, exits the program
    if  guessed_num == game_num:
        print("You guessed correctly, the number was " + str(game_num) + "!")
        if input("Do you want to play again? (enter 'yes' if you do): ").lower() == "yes":
            game_num = base_functions.generate_new_num()
            user_input = ""
        else:
            exit("Thanks for playing!")
    elif guessed_num < 1 or guessed_num > 20:            
        # if the input isn't between 1 and 20, it will inform the user and ask for another guess
        print("Please only enter a number between 1 and 20!")
    else:
        # inform the user if their guess is too high or too low and ask for another guess
        # if move mode is on, it will change the number by up to 2
        if guessed_num > game_num: print("Your guess was too high. Give it another try!")
        else: print("Your guess was too low. Give it another try!")
        if base_functions.CONFIG["MOVE_MODE_IS_ON"]:
            game_num = base_functions.move(game_num)
    
    return game_num