# ------------------------------------------------------------
# Exercise: Match AI Scientist Names
# ------------------------------------------------------------
# This program:
# 1. Reads a file of AI scientist names and stores them in a dictionary,
#    keyed by the first letter of their name.
# 2. Prompts the user for their first and last name.
# 3. Finds an AI scientist match based on the first letter of the user’s
#    first name.
# 4. Handles errors gracefully (missing file, invalid input, no match).
# ------------------------------------------------------------

def create_scientist_dict(filename="scientists.txt"):
    """
    Reads the input file and builds a dictionary mapping a letter
    (key) to an AI scientist’s name (value).
    
    Parameters:
        filename (str): Path to the file containing scientist data.
                        Expected format: "A: Alan Turing"
    
    Returns:
        dict: A dictionary with letters as keys and scientist names as values.
              Returns None if the file is not found.
    """
    scientist_dict = {}
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                if ":" in line:  # Validate format
                    key, value = line.strip().split(":", 1)
                    scientist_dict[key.strip().upper()] = value.strip()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    return scientist_dict


def get_scientist_name(scientist_dict):
    """
    Prompts the user for their first and last name,
    then finds an AI scientist match based on the first letter
    of the first name.
    
    Parameters:
        scientist_dict (dict): Dictionary of scientist matches.
    
    Returns:
        None
    """
    user_input = input("Enter your first and last name: ").strip()
    
    # Validate input
    if not user_input:
        print("Error: No input provided.")
        return
    
    first_name = user_input.split()[0]  # Use only the first word
    if not first_name.isalpha():
        print("Error: Invalid name format. Please use alphabetic characters.")
        return
    
    # Lookup based on first letter
    first_letter = first_name[0].upper()
    if first_letter in scientist_dict:
        print(f"Your AI scientist match: {scientist_dict[first_letter]}")
    else:
        print(f"No AI scientist found for the letter '{first_letter}'.")


if __name__ == "__main__":
    # Main program flow
    scientists = create_scientist_dict("scientists.txt")
    if scientists:  # Only continue if dictionary was successfully created
        get_scientist_name(scientists)
