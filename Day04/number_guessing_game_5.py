import random

#generates a random number from 1 to 20
game_num = random.randrange(1,20) 
guessed_num = ""
debug_is_on=False
move_mode_is_on=False
def non_digit_input():
    #if the input is x it will exit the program, if s it will show the number
    #if m it will toggle move mode, if d it will toggle debug mode
    #if m, d or irrelevant input, it will restart the loop
    if guessed_num == "x":
        print("Thanks for playing!")
        exit (0)
    elif guessed_num == "s" and not debug_is_on:
        print("The number is " + str(game_num))
        return "keep going"
    elif guessed_num == "m":
        move_mode_is_on = not move_mode_is_on
        print("Move mode is now", "on. The random number might change \
            by up to 2 after each guess!" if move_mode_is_on \
            else "off. The random number will not change anymore.")    
    elif guessed_num == "d":
        # Toggle debug mode
        debug_is_on = not debug_is_on
        print("Debug mode is now "+ "on." if debug_is_on else "off.")
    else:
        return "restart the loop"
def move():
    # Move mode: change the number by up to 2
    game_num = game_num + random.randint(-2, 2)
    if game_num < 1:
        game_num += 4
    elif game_num > 20:
        game_num -= 4
    print("The number has been moved by up to 2.")


#while loop to keep asking for a guess until the user guesses correctly
while guessed_num != int(game_num):
    #if debug mode is on, it will print the number
    if debug_is_on:
        print("The number is " + str(game_num))
    guessed_num = input("Enter your guess of which integer between 1-20 was generated: "); 
    
    if guessed_num.isdigit() == False:
            if non_digit_input()=="restart the loop":
                continue

    else:        
        guessed_num = int(guessed_num)
        #if the guess is correct, it will inform them and then ask if to contiue
        # if not, exits the program
        if  guessed_num == game_num:
            print("You guessed correctly, the number was " + str(game_num) + "!")
            if input(print("Do you want to play again? (enter 'yes' if you do): ")) == "y":
                game_num = random.randrange(1,20)
                guessed_num = ""
                continue
            else:
                exit("Thanks for playing!")
        
        #if the guess is too high, it will inform them and ask for another guess
        elif guessed_num > game_num:
            print("Your guess was too high. Give it another try!")
            
        elif guessed_num < game_num:
            #if the guess is not correct, it will check if it is too high or too low
            #and print the appropriate message
            print("Your guess was too low. Give it another try!")
        elif guessed_num < 1 or guessed_num > 20:            
            #if the input is between 1 and 20, it will inform the user and ask for another guess
            print("Please enter a number between 1 and 20.")
        if move_mode_is_on:
            move()