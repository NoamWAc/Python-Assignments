import random

def move(game_num):
    # Move mode: change the number by up to 2
    game_num = game_num + random.randint(-2, 2)
    if game_num < 1:
        game_num += 4
    elif game_num > 20:
        game_num -= 4
    print("The number may have increased or decreased by up to 2.")
    return game_num


if __name__ == "__main__":
    # This block is for testing purposes only
    game_num = 10  # Example number for testing
    print("Initial game number:", game_num)
    game_num = move(game_num)  # Call the move function to see the effect
    print("New game number after move:", game_num)