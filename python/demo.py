# -----------------------------------------------------------
# demo.py
# -----------------------------------------------------------
# PURPOSE:
# Demonstrates:
# 1. Importing custom modules (`useful_functions.py`).
# 2. Using functions from that module (mean, add_five).
# 3. How the special __name__ variable works in Python.
# -----------------------------------------------------------

# Import the custom module `useful_functions.py` and alias it as `uf`
import useful_functions as uf

# -----------------------------------------------------------
# Step 1: Define some test data (student scores)
# -----------------------------------------------------------
scores = [88, 92, 79, 93, 85]

# Step 2: Use functions from the imported module
# - uf.mean() computes the average of the list
# - uf.add_five() curves the scores upward by +5 points
mean = uf.mean(scores)
curved = uf.add_five(scores)

# Step 3: Compute the new mean after curving
mean_c = uf.mean(curved)

# Step 4: Print results to compare before and after
print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)

# -----------------------------------------------------------
# Step 5: Demonstrate the __name__ variable
# -----------------------------------------------------------
# - Every Python module has a built-in variable __name__.
# - When a file is run directly → __name__ == "__main__"
# - When a file is imported as a module → __name__ == module name
print(__name__)       # For demo.py → should print "__main__"
print(uf.__name__)    # For useful_functions.py → should print "useful_functions"
