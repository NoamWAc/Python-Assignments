celestial_objects = [
    'Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid'
]
words = []
count = []
for word in celestial_objects:
    if word not in words:
        words.append(word)
        count.append(1)
    else:
        count[words.index(word)] += 1

for i in range(len(words)):
    print(f"{words[i]} {count[i]}")
