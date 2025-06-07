import sys, os
from collections import Counter

# This code counts the occurrences of each digit (0-9) in a file and writes the counts to an output file.

# borrowed from Day06/rot13_file.py
def get_unique_filename(base):
    if not os.path.exists(base):
        return base
    name, ext = os.path.splitext(base)
    i = 1
    while True:
        new_name = f"{name}({i}){ext}"
        if not os.path.exists(new_name):
            return new_name
        i += 1

if len(sys.argv) < 2:
    exit(f"Usage: {sys.argv[0]} FILENAME")
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    text = f.read()

# Counter suggested by ChatGPT. Iterates over a string's characters and counts only digits, and counts unique digits.
counts = Counter(c for c in text if c.isdigit())

output_file_name = get_unique_filename('report.txt')

with open(output_file_name, 'w', encoding='utf-8') as out:
    
    # Sorts by digit, then writes the counts to the output file
    for digit in map(str, range(10)):
        out.write(f"{digit} {counts[digit]}\n")
