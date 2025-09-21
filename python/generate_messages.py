# -----------------------------------------------------------
# PROGRAM: Student Reminder Generator
# PURPOSE: Collect student data (names, missing assignments, grades)
#          and generate personalized reminder messages.
# LESSON: Demonstrates how to:
#   - Process and clean user input
#   - Convert data types
#   - Use string templates for output
#   - Loop through multiple pieces of related data at once
# -----------------------------------------------------------

# Step 1: Get input from the user
# Users will enter values separated by commas (CSV style).
# Example:
#   names       -> "Alice, Bob, Charlie"
#   assignments -> "2, 0, 5"
#   grades      -> "85, 90, 70"
names = input("Enter the names separated by commas: ").split(",")
assignments = input("Enter the number of missing assignments separated by commas: ").split(",")
grades = input("Enter the grades separated by commas: ").split(",")

# Step 2: Clean and convert data
# - Strip whitespace from each entry to handle " Bob " → "Bob"
# - Convert assignments and grades from strings → integers for calculations
assignments = [int(a.strip()) for a in assignments]
grades = [int(g.strip()) for g in grades]
names = [n.strip() for n in names]

# Step 3: Define the message template
# - {} placeholders will be replaced with actual values using .format()
# - The message reminds students about missing assignments and shows
#   how much their grade could improve if they complete them.
message = (
    "Hi {},\n\n"
    "This is a reminder that you have {} assignments left to "
    "submit before you can graduate. Your current grade is {} and can increase "
    "to {} if you submit all assignments before the due date.\n\n"
)

# Step 4: Loop through all students simultaneously
# - zip() lets us iterate over names, assignments, and grades in parallel
# - For each student, calculate potential grade:
#   potential_grade = current grade + (2 points * missing assignments)
for name, assignment, grade in zip(names, assignments, grades):
    potential_grade = grade + (2 * assignment)
    # Fill the message template with each student’s actual data
    print(message.format(name, assignment, grade, potential_grade))
