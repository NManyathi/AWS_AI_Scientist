# -----------------------------------------------------------
# Quiz: Compute an Exponent
# -----------------------------------------------------------
# Task:
# Use the math module to calculate e raised to the power of 3.
# -----------------------------------------------------------

# Step 1: Import the math module
import math

# Step 2: Use math.exp(x) to compute e^x
result = math.exp(3)

# -----------------------------------------------------------
# Notebook grading: verify the result
# -----------------------------------------------------------
correct = math.exp(3)

# Compare results up to 12 decimal places (floating-point safe)
if round(result, 12) == round(correct, 12):
    print("Nice job!")
else:
    print("Your code produced the wrong result. Expected answer is `20.085536923187668`.")

# -----------------------------------------------------------
# Quiz: Password Generator
# -----------------------------------------------------------
# Scenario:
# Generate strong but memorable passwords by concatenating
# three random words from a dictionary file (words.txt).
# -----------------------------------------------------------

# Step 1: Import the random module
import random

# Step 2: Build a list of usable words from words.txt
word_file = "words.txt"   # input file containing words
word_list = []            # global list to store valid words

with open(word_file, 'r') as words:
    for line in words:
        # Clean up the line: strip whitespace, make lowercase
        word = line.strip().lower()
        # Keep only words that are reasonably sized (4–7 chars)
        if 3 < len(word) < 8:
            word_list.append(word)


# Step 3: Define password generator function
def generate_password():
    """
    Generate a random password by concatenating
    three random words from the global word_list.
    """
    # Option 1: your approach (works fine)
    # return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

    # Option 2: cleaner with join() and list comprehension
    return "".join(random.choice(word_list) for _ in range(3))


# Step 4: Test the function
password = generate_password()
print(password)