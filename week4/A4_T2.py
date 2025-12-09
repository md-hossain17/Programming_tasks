print("Program starting.")

# Get user input for starting and stopping values
start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))

print("\nStarting for-loop:")

# Build a string with all numbers
numbers = []
for i in range(start, stop + 1):
    numbers.append(str(i))

# Print all numbers joined by spaces
print(" ".join(numbers))

print("\nProgram ending.")