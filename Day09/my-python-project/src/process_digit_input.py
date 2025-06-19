import config
import rng_1_to_20
import move_game_num



def digit_input_check(guessed_num, game_num, move_mode_available):
    """
    This function takes user's guessed number, the game number, and a boolean indicating if move mode is available.
    It returns the (possibly updated) game number based on the user's guess.

    >>> digit_input_check(5, 10, false)
    returns 10
    """
    
    # if the input isn't an int, it will convert it to an integer and check if it is correct       
    if guessed_num != int:
        guessed_num = int(guessed_num)
    # if the guess is correct, it will inform the user and then ask them if to continue
    # if yes, reset number, if not, exits the program
    if  guessed_num == game_num:
        print("You guessed correctly, the number was " + str(game_num) + "!")
        if input("Do you want to play again? (enter 'yes' if you do): ") == "yes":
            game_num = rng_1_to_20.generate_new_num()
            user_input = ""
        else:
            exit("Thanks for playing!")
    elif guessed_num < 1 or guessed_num > 20:            
        #if the input isn't between 1 and 20, it will inform the user and ask for another guess
        print("Please only enter a number between 1 and 20!")
    else:
        # inform the user if their guess is too high or too low and ask for another guess
        # if move mode is on, it will change the number by up to 2
        if guessed_num > game_num: print("Your guess was too high. Give it another try!")
        else: print("Your guess was too low. Give it another try!")
        if config.MOVE_MODE_IS_ON and move_mode_available:
            game_num = move_game_num.move(game_num)
    return game_num
