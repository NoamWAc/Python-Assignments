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
    global game_num
    global guessed_num
    global debug_is_on
    global move_mode_is_on
    if guessed_num == "x":
        print("Thanks for playing!")
        exit (0)
    elif guessed_num == "s" and not debug_is_on:
        print("The number is " + str(game_num))
        return "keep going"
    elif guessed_num == "m":
        move_mode_is_on = not move_mode_is_on
        print("Move mode is now", "on. The game's number might increase or decrease by up to 2 after each guess!" if move_mode_is_on \
            else "off. The number will not change anymore.")    
    elif guessed_num == "d":
        # Toggle debug mode
        debug_is_on = not debug_is_on
        print("Debug mode is now "+ ("on." if debug_is_on else "off."))
    else:
        return "restart the loop"

def move():
    # Move mode: change the number by up to 2
    global game_num
    game_num = game_num + random.randint(-2, 2)
    if game_num < 1:
        game_num += 4
    elif game_num > 20:
        game_num -= 4
    print("The number has been moved by up to 2.")
    return "keep going"

#while loop to keep asking for a guess until the user guesses correctly
while guessed_num != int(game_num):
    if move_mode_is_on and str(guessed_num).isdigit():
            move()
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
        