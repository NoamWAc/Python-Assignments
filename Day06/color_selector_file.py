import sys
import os

# In addition to its ability to allow users to select colors from a list, add new colors, and remove existing 
# ones interactively, this new code allows a text file to be given as a system argument. If the file exists, it will be used as the base color list. If the file is empty or unreadable, it will use a default base color list.

def load_colors_from_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip() and not line.strip().isdigit()]
    except Exception as e:
        print(f"Error reading color file: {e}")
        return None


def show_menu(colors, last_selected):
    print("\nColor Menu:")
    for i, color in enumerate(colors, start=1):
        print(f"{i}. {color}")
    print("a. Add a color")
    print("r. Remove a color")
    print("q. Quit")
    if last_selected:
        print(f"(Last selected: {last_selected})")

def get_color_from_input(user_input, colors):
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

def add_color_interactive(colors):
    name = input("Enter a new color to add: ").strip()
    if not name:
        print("Empty name ignored.")
        return
    if name.isdigit():
        print("Color names can't be made of only numbers.")
        return
    if name.lower() in (c.lower() for c in colors):
        print(f"Color '{name}' already exists.")
    else:
        colors.append(name)
        print(f"Added color: {name}")


def remove_color_interactive(colors, base_colors):
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
    args = sys.argv[1:]
    default_base = ['blue', 'green', 'yellow', 'white']

    colors = []
    base_colors = []

    # If a file is provided, use it for base colors
    if args and os.path.isfile(args[0]):
        file_colors = load_colors_from_file(args[0])
        if file_colors:
            colors = file_colors.copy()
            base_colors = file_colors.copy()
            args = args[1:]  # remove file path from remaining args
        else:
            print("File empty or unreadable. Using default base colors.")
    else:
        colors = default_base.copy()
        base_colors = default_base.copy()

    last_selected = None

    # Try to select a color if another argument was passed
    if args:
        selection = get_color_from_input(args[0], colors)
        if selection:
            last_selected = selection
            print(f"Selected color: {selection}")

    # Main interaction loop
    while True:
        show_menu(colors, last_selected)
        choice = input("Choose a number, name, or action (a/r/q): ").strip().lower()

        if choice == 'q':
            print("Goodbye.")
            break
        elif choice == 'a':
            add_color_interactive(colors)
        elif choice == 'r':
            remove_color_interactive(colors, base_colors)
        else:
            selected = get_color_from_input(choice, colors)
            if selected:
                last_selected = selected
                print(f"Selected color: {selected}")

if __name__ == '__main__':
    main()
