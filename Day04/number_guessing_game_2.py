import random

#generates a random number from 1 to 20
target_num = random.randrange(1,20) 
guessed_num = "0"

#while loop to keep asking for a guess until the user guesses correctly
while int(guessed_num) != target_num:
    #asks user for their guess and converts input to int
    guessed_num = input("Enter your guess of which integer between 1-20 was generated: "); 
    if guessed_num == "x":
        print("Thanks for playing!")
        exit (0)
    guessed_num = int(guessed_num)
    #if the guess is correct, it will inform them and then exit the program
    if  guessed_num == target_num:
        print("You guessed correctly! The number really was ", guessed_num, "!")
        print("Thanks for playing!")
        exit (0)

    elif guessed_num > target_num:
        print("Your guess was too high. Give it another try!")
        
    else:
        #if the guess is not correct, it will check if it is too high or too low
        #and print the appropriate message
        print("Your guess was too low. Give it another try!")

    
    

