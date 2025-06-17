import config
import initialize
def non_digit_input_check(game_num, guessed_num):
    '''
    if the input is x it will exit the program, if s it will show the number
    if m it will toggle move mode, if d it will toggle debug mode
    if m, d or irrelevant input, it will restart the loop
    '''
    if guessed_num == "x":
        print("Thanks for playing!")
        exit (0)
    elif guessed_num == "n":
        game_num=initialize()
        print("The game has been reset.")
        return game_num
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
