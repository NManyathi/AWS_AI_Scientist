# -----------------------------------------------------------
# FILE HANDLING IN PYTHON
# -----------------------------------------------------------
# This script demonstrates:
# 1. Opening and reading files manually
# 2. Using `with open(...)` (the safer approach)
# 3. Writing to a file
# 4. A bad example that causes resource leaks
# -----------------------------------------------------------

# -----------------------------------------------------------
# 1. Manual open, read, close
# -----------------------------------------------------------
# You can open a file using open(), read its content, then close it.
# The problem: If you forget f.close(), the file stays open,
# which can lock the file or cause memory leaks.
f = open('C:/Users/Naspers_Labs/Desktop/Udacity/AWS_AI_Scientist/python/some_file.txt', 'r')
file_data = f.read()
print(file_data)
f.close()  # Must close manually


# -----------------------------------------------------------
# 2. Safer alternative: `with open(...)` context manager
# -----------------------------------------------------------
# The `with` statement automatically closes the file when finished,
# even if an error occurs inside the block. This is the recommended way.
with open('C:/Users/Naspers_Labs/Desktop/Udacity/AWS_AI_Scientist/python/some_file.txt', 'r') as f:
    file_data = f.read()
    print(file_data)  # You can use file_data here safely


# -----------------------------------------------------------
# 3. Writing to a file
# -----------------------------------------------------------
# Mode 'w' means "write" → it will overwrite the file if it exists,
# or create a new file if it doesn’t exist.
f = open('C:/Users/Naspers_Labs/Desktop/Udacity/AWS_AI_Scientist/python/my_file.txt', 'w')
f.write("Hello there!")  # Writing string data into the file
f.close()  # Always close when using open() without `with`


# -----------------------------------------------------------
# 4. BAD EXAMPLE: Opening too many files without closing
# -----------------------------------------------------------
# This loop keeps opening the same file but never closes it.
# Every iteration adds another open file object into memory.
# This will eventually raise an OSError:
# "Too many open files" → because the OS limits open handles.
"""files = []
for i in range(10000):
    files.append(open('some_file.txt', 'r'))  # file never closed!
    print(i)"""
