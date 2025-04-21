# circle.py

import math
import sys

radius = sys.argv[1] # Get argument

try:
    radius = float(radius) # Convert the argument to a float, exit program if can't convert
except ValueError:
    print("Invalid input. Please enter a numeric value for the radius.")
    sys.exit(1)

# Calculate area and circumference
area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

# Print the results
print(f"Area of the circle: {area:.2f}")
print(f"Circumference of the circle: {circumference:.2f}")
