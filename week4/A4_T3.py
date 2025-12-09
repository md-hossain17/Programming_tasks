print("Program starting.")

# Get user input for starting and stopping values
start = int(input("Insert starting value: "))
stop = int(input("Insert starting value: "))

print("\nStarting while-loop:")

# Initialize counter and result string
current = start
result = ""

# Use while-loop to build the result string
while current <= stop:
    result += str(current)
    if current < stop:  # Add space only if not the last number
        result += " "
    current += 1

# Print the final result
print(result)

print("\nProgram ending.")