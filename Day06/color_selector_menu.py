import sys

# Base colors (protected)
base_colors = ['blue', 'green', 'yellow', 'white']
colors = base_colors.copy()

last_selected = None  # Tracks last selected color

def show_menu():
    print("\nColor Menu:")
    for i, color in enumerate(colors, start=1):
        print(f"{i}. {color}")
    print("a. Add a color")
    print("r. Remove a color")
    print("q. Quit")
    if last_selected:
        print(f"(Last selected: {last_selected})")

def get_color_from_input(user_input):
    try:
        index = int(user_input)
        if 1 <= index <= len(colors):
            return colors[index - 1]
        else:
            print("Number out of range.")
    except ValueError:
        color = user_input.strip().lower()
        for c in colors:
            if c.lower() == color:
                return c
        print("Unknown color name.")
    return None

def add_color_interactive():
    name = input("Enter a new color to add: ").strip()
    if not name:
        print("Empty name ignored.")
        return
    if name.lower() in (c.lower() for c in colors):
        print(f"Color '{name}' already exists.")
    else:
        colors.append(name)
        print(f"Added color: {name}")

def remove_color_interactive():
    name = input("Enter a color to remove: ").strip()
    if name.lower() in (c.lower() for c in base_colors):
        print(f"Cannot remove base color '{name}'.")
        return
    for i, c in enumerate(colors):
        if c.lower() == name.lower():
            del colors[i]
            print(f"Removed color: {c}")
            return
    print(f"Color '{name}' not found.")

def main():
    global last_selected
    args = sys.argv[1:]

    # Try to select from CLI arg if given
    if args:
        selection = get_color_from_input(args[0])
        if selection:
            last_selected = selection
            print(f"Selected color: {selection}")

    # Interactive loop
    while True:
        show_menu()
        choice = input("Choose a number, name, or action (a/r/q): ").strip().lower()

        if choice == 'q':
            print("Goodbye.")
            break
        elif choice == 'a':
            add_color_interactive()
        elif choice == 'r':
            remove_color_interactive()
        else:
            selected = get_color_from_input(choice)
            if selected:
                last_selected = selected
                print(f"Selected color: {selected}")
                continue

if __name__ == '__main__':
    main()
