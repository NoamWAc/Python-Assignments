celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]

words = []
count = []
# This code counts the occurrences of words (strings) in a list and prints the count for each unique object.
# It initializes two lists: one for unique words and another for their counts.

for word in celestial_objects:
    if word not in words:
        words.append(word)
        count.append(1)
    else:
        count[words.index(word)] += 1

# Print the unique words and their counts
for i in range(len(words)):
    print(f"{words[i]} {count[i]}")
