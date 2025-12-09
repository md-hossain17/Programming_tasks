print("Program starting.")
num = int(input("Insert a positive integer: "))

# Initialize variables
sequence = [num]
steps = 0

# Generate Collatz sequence
current = num
while current != 1:
    if current % 2 == 0:  # Even
        current = current // 2
    else:  # Odd
        current = 3 * current + 1
    sequence.append(current)
    steps += 1

# Format the sequence with arrows
sequence_str = " -> ".join(str(n) for n in sequence)

# Print the results
print(f"{sequence_str}")
print(f"Sequence had {steps} total steps.")
print()
print("Program ending.")