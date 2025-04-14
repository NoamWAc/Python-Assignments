# circle.py

import math
import sys

# Ask the user for the radius
##radius = float(input("Enter the radius of the circle: "))
radius = sys.argv[1]
try:
    radius = float(radius) # Convert the input to a float
except ValueError:
    print("Invalid input. Please enter a numeric value for the radius.")
    sys.exit(1)

# Calculate area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Print the results
print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")
