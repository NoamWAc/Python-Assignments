import random
def generate_new_num():
        """
        This function generates a new random number between 1 and 20.
        >>> generate_new_num()
        returns a random integer between 1 and 20
        """        
        return random.randrange(1,20)

if __name__ == "__main__":
    print("The generated number is: " + str(generate_new_num()))
    # This is just for testing purposes, you can remove this line if you want
    # or replace it with a call to the main function of your game.

