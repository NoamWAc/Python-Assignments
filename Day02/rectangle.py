# rectangle.py

# Ask the user for height and width
height = float(input("Enter the height of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area and perimeter
area = height * width
perimeter = 2 * (height + width)

# Print the results, 2 decimal points
print(f"Area of the rectangle: {area:.2f}")
print(f"Perimeter of the rectangle: {perimeter:.2f}")
