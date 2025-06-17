import random
import os
import non_digit_input
import initialize


# Try to import move mode, but if it doesn't exist, just print a message
try:
     import move_game_num
except:
     print("move_game_num module is not available.")


#while loop to keep asking for a guess until the user guesses correctly
def interactive_number_guessing_game():
    game_num = initialize.initialize_game()
    import config
    guessed_num = ""
    while int(guessed_num) != game_num:
        if config.MOVE_MODE_IS_ON and str(guessed_num).isdigit():
                game_num = move_game_num(game_num)
        #if debug mode is on, it will print the number
        if config.DEBUG_MODE_IS_ON:
            print("The number is currently " + str(game_num))
        guessed_num = input("Enter your guess of which integer between 1-20 was generated: "); 
        
        if guessed_num.isdigit() == False:
                if non_digit_input.non_digit_input_check()=="restart the loop":
                    continue

        else:        
            guessed_num = int(guessed_num)
            #if the guess is correct, it will inform them and then ask if to contiue
            # if not, exits the program
            if  guessed_num == game_num:
                print("You guessed correctly, the number was " + str(game_num) + "!")
                if input(print("Do you want to play again? (enter 'yes' if you do): ")) == "yes":
                    game_num = random.randrange(1,20)
                    guessed_num = ""
                    continue
                else:
                    exit("Thanks for playing!")
            elif guessed_num < 1 or guessed_num > 20:            
                #if the input isn't between 1 and 20, it will inform the user and ask for another guess
                print("Please only enter a number between 1 and 20!")
                continue
            #if the guess is too high, it will inform them and ask for another guess
            elif guessed_num > game_num:
                print("Your guess was too high. Give it another try!")
                continue
            elif guessed_num < game_num:
            #if the guess is too low, it will inform them and ask for another guess
                print("Your guess was too low. Give it another try!")
                continue
        