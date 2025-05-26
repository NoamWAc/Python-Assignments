numbers = [1203, 1256, 312456, 98]

digit_counts = [0] * 10
for number in numbers:
    for digit in str(number):
        digit_counts[int(digit)] += 1

for digit, count in enumerate(digit_counts):
    print(f"{digit} {count}")
# This code counts the occurrences of each digit (0-9) in a list of numbers and prints the count for each digit.
# It initializes a list of counts for each digit, iterates through each number, and updates the count for each digit found in the number.
