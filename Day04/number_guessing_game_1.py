import random

#generates a random number from 1 to 20
game_num = random.randrange(1,20) 
guessed_num = 0

#while loop to keep asking for a guess until the user guesses correctly
while guessed_num != game_num:
    #asks user for their guess and converts input to int
    guessed_num = int(input("Enter your guess of which integer between 1-20 was generated: ")); 

    #if the guess is correct, it will inform them and then exit the program
    if  guessed_num == game_num:
        print("You guessed correctly! The number really was ", guessed_num, "!")
        print("Thanks for playing!")
        exit (0)

    elif guessed_num > game_num:
        print("Your guess was too high. Give it another try!")
        
    else:
        #if the guess is not correct, it will check if it is too high or too low
        #and print the appropriate message
        print("Your guess was too low. Give it another try!")

    
    

