import random

game_num = random.randrange(1,20) #generated a random number from 1 to 20

guessed_num = (int(input("Enter your guess of which integer between 1-20 was generated! ")) #asks user for their guess and converts to int

if  guessed_num == game_num:
               print("You guessed correctly! The number really was ", guessed_num, "!")
               elif guessed_num > game_num
