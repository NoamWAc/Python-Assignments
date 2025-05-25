
import re

dNTPs = {'A', 'T', 'C', 'G'}  # List of valid DNA nucleotides

def get_valid_sequence():
    """
    Function to get a valid DNA sequence from the user.
    It ensures that the sequence contains only valid characters and is not empty.
    """
    while True:
        entered_sequence = input("Enter a DNA sequence: ").upper().replace(" ", "")  # Convert input sequence to uppercase for consistency, remove spaces

        if entered_sequence == "":
            print("Empty input is not allowed. Try again.")
            continue
        else:
            return entered_sequence
        
entered_sequence = get_valid_sequence()

fragmented = re.split(f'[^{dNTPs}]+', entered_sequence)  # Split the sequence by 'X', allowing for multiple consecutive 'X's
fragmented = [seq for seq in fragmented if seq]  # Remove empty sequences from the list
fragmented_by_length = sorted(fragmented, key=len)  # Sort the split sequences by length
print("The sequence split by 'X' is:", fragmented)
print("The sequence split by 'X' and sorted by length is:", fragmented_by_length)
