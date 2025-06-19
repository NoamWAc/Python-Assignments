import random
import os
import non_digit_input
import initialize
import rng_1_to_20

# Try to import move mode, but if it doesn't exist, just notify and don't enable the option
move_mode_available = False
try:
     import move_game_num
     move_mode_available = True
except:
     print("move_game_num module is not available.")

def interactive_number_guessing_game():
    game_num = initialize.initialize_game()
    import config
    user_input = ""
    while True:  
        #if debug mode is on, it will print the number
        if config.DEBUG_MODE_IS_ON:
            print("The number is currently " + str(game_num))
        
        user_input = input("Enter your guess of which integer between 1-20 was generated: ")
        
        if user_input.isdigit() == False: # if the input is not a digit, it will check if it is a special command
            game_num = non_digit_input.non_digit_input_check(user_input, game_num, move_mode_available)
            continue
            
        else: # if the input is a digit, it will convert it to an integer and check if it is correct       
            guessed_num = int(user_input)
            # if the guess is correct, it will inform the user and then ask them if to continue
            # if yes, reset number, if not, exits the program
            if  guessed_num == game_num:
                print("You guessed correctly, the number was " + str(game_num) + "!")
                if input("Do you want to play again? (enter 'yes' if you do): ") == "yes":
                    game_num = rng_1_to_20.generate_new_num()
                    user_input = ""
                    continue
                else:
                    exit("Thanks for playing!")
            elif guessed_num < 1 or guessed_num > 20:            
                #if the input isn't between 1 and 20, it will inform the user and ask for another guess
                print("Please only enter a number between 1 and 20!")
                continue
            else:
                # inform the user if their guess is too high or too low and ask for another guess
                # if move mode is on, it will change the number by up to 2
                if guessed_num > game_num: print("Your guess was too high. Give it another try!")
                else: print("Your guess was too low. Give it another try!")
                if config.MOVE_MODE_IS_ON and move_mode_available:
                    game_num = move_game_num.move(game_num)
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
    game_num = rng_1_to_20.generate_new_num()
    print("Newly generated game number:", game_num)
    non_digit_input.non_digit_input_check("help") # This should show the help message
    non_digit_input.non_digit_input_check("n") # This should reset the game
    non_digit_input.non_digit_input_check("s") # This should show the current number
    non_digit_input.non_digit_input_check("m") # This should toggle move mode
    non_digit_input.non_digit_input_check("d") # This should toggle debug mode
    non_digit_input.non_digit_input_check("invalid input") # This should restart the loop
    non_digit_input.non_digit_input_check("") # This should restart the loop
    non_digit_input.non_digit_input_check(123) # This should raise a TypeError
    non_digit_input.non_digit_input_check("x") # This should exit the program
