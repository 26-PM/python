#  Write a Python program to set a random seed and get a random
#  number between 0 and 1. Use random.random.
import random
# set a random seed
random.seed(1)

# get a random number between 0 and 1
print(random.random())












# Write a Python program to create a list of random integers and
# randomly select multiple items from the said list. Use
# random.sample()
import random
list=[random.randint(1,10) for i in range(10)]
#select 2 items
selected=random.sample(list,2)
print(selected)











# Write a Python program to configure the rounding to round to the
# floor, ceiling. Use decimal ROUND FLOOR
# decimal.ROUND_CEILING

import decimal

# Function to configure rounding
def configure_rounding(number, rounding_mode):
    return decimal.Decimal(number).quantize(decimal.Decimal('1.'), rounding=rounding_mode)

# Example usage
number_to_round = '5.999'  # Represented as a string to avoid floating-point inaccuracies

# Configure rounding to floor
rounded_floor = configure_rounding(number_to_round, decimal.ROUND_FLOOR)
print(f"Rounded to Floor: {rounded_floor}")

# Configure rounding to ceiling
rounded_ceiling = configure_rounding(number_to_round, decimal.ROUND_CEILING)
print(f"Rounded to Ceiling: {rounded_ceiling}")










# Write a Python program to select a random element from a list, set,
# dictionary-value, and file from a directory. Use random.choice()

import random
import os

# Selecting a random element from a list
my_list = [10, 20, 30, 40, 50]
random_from_list = random.choice(my_list)
print(f"Random element from list: {random_from_list}")

# Selecting a random element from a set
my_set = {1, 2, 3, 4, 5}
random_from_set = random.choice(list(my_set))
print(f"Random element from set: {random_from_set}")

# Selecting a random element from a dictionary's values
my_dict = {'a': 100, 'b': 200, 'c': 300}
random_from_dict = random.choice(list(my_dict.values()))
print(f"Random element from dictionary values: {random_from_dict}")

# Selecting a random file from a directory
directory_path = "/path/to/your/directory"  # Replace with the actual path
files_in_directory = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

if files_in_directory:
    random_file = random.choice(files_in_directory)
    print(f"Random file from directory: {random_file}")
else:
    print("No files in the specified directory.")









# Write a Python Program that implements all the functions of Math
# module


import math

# Example usage of some math functions
number = 4.7

# Basic arithmetic operations
print(f"Square root of {number}: {math.sqrt(number)}")
print(f"Ceiling of {number}: {math.ceil(number)}")
print(f"Floor of {number}: {math.floor(number)}")
print(f"Factorial of {int(number)}: {math.factorial(int(number))}")

# Trigonometric functions
angle_in_radians = math.radians(45)
print(f"Sine of 45 degrees: {math.sin(angle_in_radians)}")
print(f"Cosine of 45 degrees: {math.cos(angle_in_radians)}")
print(f"Tangent of 45 degrees: {math.tan(angle_in_radians)}")

# Logarithmic and exponential functions
print(f"Natural logarithm of {number}: {math.log(number)}")
print(f"10-base logarithm of {number}: {math.log10(number)}")
print(f"Exponential of {number}: {math.exp(number)}")

# Power and absolute functions
base = 2
exponent = 3
print(f"{base} raised to the power of {exponent}: {math.pow(base, exponent)}")
print(f"Absolute value of {number}: {math.fabs(number)}")
