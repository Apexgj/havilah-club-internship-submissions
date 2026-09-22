# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# TODO: name = "Alice"  # string
name = "Alice"
age = 30
height = 5.6
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

# TODO: celsius = float(input("Enter temperature in Celsius: "))
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print(f"Temperature in Celsius: {celsius}")

# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

# TODO: name = input("Enter your name: ")
# TODO: birth_year = int(input("Enter your birth year: "))

name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_age = 2023 - birth_year
year_turn_30 = birth_year + 30

print(f"Hello, {name}!")
print(f"You are currently {current_age} years old.")
print(f"You will turn 30 in the year {year_turn_30}.")

print("All exercises completed successfully!")
