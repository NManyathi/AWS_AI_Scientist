"""
CODE EXPLANATION – TWO APPROACHES TO PROBLEM SOLVING

This script demonstrates that there are often multiple ways to solve a problem.
We show TWO approaches:

1. Function-Based Approach (resource_allocator + main)
   - Uses functions to organize logic.
   - Includes error handling, input validation, and a loop for repeated use.
   - Better for larger programs or when you need to reuse code.

2. Direct Loop Approach (user_list + sum calculation)
   - Simpler and more direct.
   - Reads inputs, processes them immediately, and gives an output.
   - Works well for small, one-time scripts but is less reusable.

>>> WHICH IS BETTER?
- For small exercises or quick calculations → the direct loop approach is fine.
- For professional projects, teamwork, or future scaling → the function-based 
  approach is better because:
    * It separates logic from user interaction.
    * It makes debugging and testing easier.
    * It allows reuse of the same function in other scripts.
"""

# -------------------------------
# FIRST APPROACH: FUNCTION-BASED
# -------------------------------

def resource_allocator(resources, tasks):
    """Allocates resources to tasks and handles division by zero errors."""
    try:
        # Prevent dividing by zero by manually raising an error if tasks == 0
        if tasks == 0:
            raise ZeroDivisionError("Number of tasks cannot be zero.")

        # Integer division to calculate how many resources each task gets
        resources_per_task = resources // tasks  

        # Find leftovers that cannot be evenly distributed
        leftovers = resources % tasks  

        # Return both results
        return resources_per_task, leftovers

    except ZeroDivisionError as e:
        # Print the custom error message and return placeholders
        print(e)
        return None, None


# The main function handles user interaction and loops until user quits
def main():
    lets_optimize = 'y'  # control variable to continue or exit the loop
    while lets_optimize == 'y':
        try:
            # Ask user for number of resources
            resources = int(input("How many computational resources (computers) are available? "))
            if resources < 0:  # validation: no negatives
                print("Number of resources cannot be negative. Please enter a positive number.")
                continue  # restart loop

            # Ask user for number of tasks
            tasks = int(input("How many tasks (people) need resources? "))
            if tasks < 0:  # validation: no negatives
                print("Number of tasks cannot be negative. Please enter a positive number.")
                continue  # restart loop

            # Call resource allocator function
            resources_each, leftovers = resource_allocator(resources, tasks)

            # Only print results if allocation succeeded
            if resources_each is not None:
                message = "\nResource Allocation: We'll have {} tasks, each will get {} resources, and we'll have {} resources left over."
                print(message.format(tasks, resources_each, leftovers))

            # Ask user if they want to repeat
            lets_optimize = input("\nWould you like to optimize more? (y or n) ").lower()

        except ValueError:
            # Handle invalid (non-numeric) input
            print("Invalid input. Please enter a valid number.")


# Only run main if script is executed directly
if __name__ == "__main__":
    main()


# -------------------------------
# SECOND APPROACH: DIRECT LOOP
# -------------------------------

"""
This second part demonstrates a simpler, direct loop approach.
Instead of creating a function, it:
- Collects numbers into a list
- Adds only the even numbers
- Prints both the full list and the sum
"""

user_list = []  # list to store user numbers
list_sum = 0    # accumulator for even numbers

for _ in range(10):  # ask for 10 numbers
    try:
        userInput = int(input("Enter any number: "))
    except ValueError:  
        # If conversion fails, skip this round
        print("Incorrect value. That's not an int!")
        continue  

    user_list.append(userInput)  # add to list

    # If the number is even, add it to the running total
    if userInput % 2 == 0:
        list_sum += userInput

# Final outputs
print(f"user_list: {user_list}")
print(f"The sum of the even numbers in user_list is: {list_sum}.")
