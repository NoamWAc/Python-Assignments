import sys
import collections

# This script counts the occurrences of each word in a given text file.

if len(sys.argv) < 2:
    print("Usage: python count_words_from_a_file.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r', encoding='utf-8') as text_file:
        text = text_file.read()
except FileNotFoundError:
    print(f"File '{filename}' not found.")
    sys.exit(1)

# Split by whitespace and normalize to lowercase
words = text.lower().split()

# Count occurrences
counter = collections.Counter(words)

# Print counts
for word, count in sorted(counter.items()):
    print(f"{word} {count}")
