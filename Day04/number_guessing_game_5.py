import random

#generates a random number from 1 to 20
game_num = random.randrange(1,20) 

#asks user for their guess and converts input to int
guessed_num = int(input("Enter your guess of which integer between 1-20 was generated! ")); 

if  guessed_num == game_num:
    print("You guessed correctly! The number really was ", guessed_num, "!")
elif guessed_num > game_num:
    print("Your guess was too high!")
else:
    #if the guess is not correct, it will check if it is too high or too low
    #and print the appropriate message
    #it will also print the number that was generated
    #so the user can see what they were guessing against
    #and then exit the program
    print("Your guess was too low!")
    print("The number was ", game_num)
    print("Thanks for playing!")
    exit (0);