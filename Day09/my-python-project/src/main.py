import base_functions
import process_input
import process_input


def interactive_number_guessing_game():
    """
    This function runs an interactive number guessing game where the user has to guess a randomly-generated number between 1 and 20.
    """
    game_num = base_functions.initialize_game()
    user_input = ""
    
    while True:  
        #if debug mode is on, it will print the number
        if base_functions.CONFIG["DEBUG_MODE_IS_ON"]:
            print("The number is currently " + str(game_num))
        
        user_input = input("Enter your guess of which integer between 1-20 was generated: ")
        
        if user_input.isdigit() == False: # if the input is not a digit, it will check if it is a special command
            game_num = process_input.non_digit_input_check(user_input, game_num)
            continue   
        else:
            game_num = process_input.digit_input_check(int(user_input), game_num) # if the input is a digit, it will process it
            continue
    raise Exception ("An error occurred. To avoid infinite loop, please troubleshoot or try again.") # if the loop is not working properly, it will raise an exception to avoid infinite loop



if __name__ == "__main__":
    interactive_number_guessing_game()