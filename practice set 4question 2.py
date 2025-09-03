# Input marks of six students separated by spaces
marks = input("Enter marks of six students separated by spaces: ").split()

# Convert the input strings to integers
marks = [int(mark) for mark in marks]

# Print the list of marks before sorting
print("Marks before sorting:", marks)

# Sort the marks in ascending order
marks.sort()

# Print the sorted list of marks
print("Marks after sorting:", marks)
