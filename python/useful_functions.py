# -----------------------------------------------------------
# useful_functions.py
# -----------------------------------------------------------
# PURPOSE:
# A small helper module that provides reusable functions:
#   - mean(): calculate the average of a list of numbers
#   - add_five(): add +5 to each number in a list
#
# Includes a test suite in the main() function to verify correctness.
# -----------------------------------------------------------

def mean(num_list):
    """
    Calculate the arithmetic mean (average) of a list of numbers.
    
    Args:
        num_list (list of int/float): List of numeric values.
    
    Returns:
        float: The average value.
    """
    return sum(num_list) / len(num_list)


def add_five(num_list):
    """
    Add 5 to every number in the given list.
    
    Args:
        num_list (list of int/float): List of numeric values.
    
    Returns:
        list: New list with each element increased by 5.
    """
    return [n + 5 for n in num_list]


def main():
    """
    Simple test suite for the functions in this module.
    Uses Python's assert statements to confirm that the
    functions return the expected results.
    """
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert mean(n_list) == correct_mean, "mean() test failed!"

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert add_five(n_list) == correct_list, "add_five() test failed!"

    print("All tests passed!")


# -----------------------------------------------------------
# When run directly (python useful_functions.py), main() executes.
# When imported (e.g., in demo.py), main() does not run, so only
# the functions are available for use.
# -----------------------------------------------------------
if __name__ == '__main__':
    main()
