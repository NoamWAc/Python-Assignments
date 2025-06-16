import os
print("Working directory:", os.getcwd())
import color_selector
def main():
    colors, base_colors = color_selector.initialize_colors()
    last_selected = None
    while True:
    # Show the menu and get user input
        color_selector.show_menu(colors, last_selected)
        colors, last_selected = color_selector.user_interact(colors, base_colors)

if __name__ == '__main__':
    main()