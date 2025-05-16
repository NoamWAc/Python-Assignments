import random

#generates a random number from 1 to 20
game_num = random.randrange(1,20) 
guessed_num = "0"
is_debug_on=False


#while loop to keep asking for a guess until the user guesses correctly
while guessed_num != int(game_num):
    #asks user for their guess and converts input to int
    if is_debug_on:
        print("The number is " + str(game_num))
    guessed_num = input("Enter your guess of which integer between 1-20 was generated: "); 
    
    if guessed_num == "x":
        print("Thanks for playing!")
        exit (0)
    elif guessed_num == "s":
        print("The number is " + str(game_num))
    elif guessed_num == "d":
        # Toggle debug mode
        is_debug_on = not is_debug_on
        print("Debug mode is now", "on." if is_debug_on else "off.")
        continue
        
    else:
        if guessed_num.isdigit() == False:
            print("Please enter a number between 1 and 20.")
            continue
        guessed_num = int(guessed_num)
        #if the guess is correct, it will inform them and then exit the program
        if  guessed_num == game_num:
            print("You guessed correctly, the number was " + str(game_num) + "!")
            exit ("Thanks for playing!")
        #if the guess is too high, it will inform them and ask for another guess
        
        elif guessed_num > game_num:
            print("Your guess was too high. Give it another try!")
            
        elif guessed_num < game_num:
            #if the guess is not correct, it will check if it is too high or too low
            #and print the appropriate message
            print("Your guess was too low. Give it another try!")
        else:
            #if the input is between 1 and 20, it will inform the user and ask for another guess
            print("Please enter a number between 1 and 20.")