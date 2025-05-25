

allowed_chars = {'A', 'T', 'C', 'G', 'X'}  # List of valid DNA nucleotides

while True:
    entered_sequence = input("Enter a DNA sequence: ").upper().replace(" ", "") # Convert input sequence to uppercase for consistency, remove spaces

    if entered_sequence == "":
        print("Empty input is not allowed. Try again.")
        continue
    if not all(char in allowed_chars for char in entered_sequence):
        print("Invalid characters detected. Please enter a valid DNA sequence containing only A, T, C, G, or X.")
        continue
    else:
        break

minus_X = entered_sequence.split('X')  # Split the sequence by 'X'
minus_X = [seq for seq in minus_X if seq]  # Remove empty sequences from the list
minus_X_by_length = sorted(minus_X, key=len, reverse=True)  # Sort the split sequences by length
print("The sequence split by 'X' is:", minus_X)
print("The sequence split by 'X' and sorted by length is:", minus_X_by_length)
