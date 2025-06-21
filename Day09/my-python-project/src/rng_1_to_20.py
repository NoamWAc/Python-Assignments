import random
def generate_new_num():
        """
        This function generates a new random number between 1 and 20.
        >>> random.seed(0)  # For reproducibility in tests
        >>> generate_new_num()
        13
        """        
        return random.randrange(1,20)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

