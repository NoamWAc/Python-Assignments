# rectangle.py
import sys

# Ask the user for height and width
#height = float(input("Enter the height of the rectangle: "))
#width = float(input("Enter the width of the rectangle: "))

height = sys.argv[1]
width = sys.argv[2]
try:
    height = float(height) # Convert the input to a float
    width = float(width) # Convert the input to a float
except ValueError:
    print("Invalid input. Please enter numeric values for height and width.")
    sys.exit(1)

# Calculate area and perimeter
area = height * width
perimeter = 2 * (height + width)

# Print the results, 2 decimal points
print(f"Area of the rectangle: {area:.2f}")
print(f"Perimeter of the rectangle: {perimeter:.2f}")
