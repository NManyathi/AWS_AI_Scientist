def create_scientist_list(filename):
    """
    Reads a text file and extracts a list of AI scientist names.

    Each line in the file is assumed to have the format:
        "Name, Other Information"
    For example:
        "Alan Turing, Mathematician"
    Only the name (the first value before the comma) is kept.
    """
    scientist_list = []  # initialize an empty list to store names

    # Use a try/except block in case the file is missing
    try:
        # 'with' ensures the file is automatically closed after reading
        with open(filename, 'r') as file:
            # Loop through each line in the file
            for line in file:
                # Split the line into parts separated by commas
                parts = line.split(',')
                if parts:
                    # Take the first part (the scientist's name)
                    # Strip removes spaces or newline characters
                    name = parts[0].strip()
                    scientist_list.append(name)

    except FileNotFoundError:
        # Gracefully handle the case when the file is not found
        print(f"The file {filename} was not found.")

    # Return the comple
