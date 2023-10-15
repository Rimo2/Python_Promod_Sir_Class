# Write a Python program to calculate the area of a circle given its radius using the formula
# area=π×r^2 ( Take pie as 3.14)

rad = int(input('Enter the desired radius:\n'))
pi = 3.1416
area = pi * (rad ** 2)
print('The area of the circle with radius ' + str(rad) + ' is ' + str(area))

# Trying to make it better
import math

radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = math.pi * (radius ** 2)

# Print the result
print(f"The area of the circle with radius {radius} is {area:.3f}")
print('The value of pi is ' + str(math.pi))
