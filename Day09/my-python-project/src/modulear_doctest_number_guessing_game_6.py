import process_non_digit_input
import process_digit_input
import initialize


print("Welcome to the interactive number guessing game!")

# Try to import move mode, but if it doesn't exist, just notify and don't enable the option
move_mode_available = False
try:
     import move_game_num
     move_mode_available = True
except:
     print("move_game_num module is not available. Move mode will not be enabled in this instance of the game.")

def interactive_number_guessing_game():
    """
    This function runs an interactive number guessing game where the user has to guess a number between 1 and 20.
    """
    game_num = initialize.initialize_game()
    import config
    print("To access additional features, enter command when asked to enter your guess. Enter 'help' to see available commands.")
    user_input = ""
    while True:  
        #if debug mode is on, it will print the number
        if config.DEBUG_MODE_IS_ON:
            print("The number is currently " + str(game_num))
        
        user_input = input("Enter your guess of which integer between 1-20 was generated: ")
        
        if user_input.isdigit() == False: # if the input is not a digit, it will check if it is a special command
            game_num = process_non_digit_input.non_digit_input_check(user_input, game_num, move_mode_available)
            continue   
        else:
            game_num = process_digit_input.digit_input_check(int(user_input), game_num, move_mode_available) # if the input is a digit, it will process it
            continue
    raise Exception ("An error occurred. To avoid infinite loop, please troubleshoot or try again.") # if the loop is not working properly, it will raise an exception to avoid infinite loop

def test():
    """
    This function is for testing purposes only.
    """
    game_num = initialize.initialize_game()
    print("Initial game number:", game_num)
    game_num = move_game_num.move(game_num) if move_mode_available else game_num
    print("New game number after move:", game_num)
    import rng_1_to_20
    game_num = rng_1_to_20.generate_new_num()
    print("Newly generated game number:", game_num)
    process_non_digit_input.non_digit_input_check("help") # This should show the help message
    process_non_digit_input.non_digit_input_check("n") # This should reset the game
    process_non_digit_input.non_digit_input_check("s") # This should show the current number
    process_non_digit_input.non_digit_input_check("m") # This should toggle move mode
    process_non_digit_input.non_digit_input_check("d") # This should toggle debug mode
    process_non_digit_input.non_digit_input_check("invalid input") # This should restart the loop
    process_non_digit_input.non_digit_input_check("") # This should restart the loop
    process_non_digit_input.non_digit_input_check(123) # This should raise a TypeError
    process_non_digit_input.non_digit_input_check("x") # This should exit the program