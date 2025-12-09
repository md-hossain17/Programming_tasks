print("Program starting.")

# Get user input
start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))

# Initialize error flag
has_error = False

# Rule 1: Starting point must be less than stopping point
if start >= stop:
    print("Starting point value must be less than the stopping point value.")
    has_error = True

# Rule 2: Inspection point must be within the range
if inspect < start or inspect > stop:
    print("Inspection value must be within the range of start and stop.")
    has_error = True

# If no errors, run the loops
if not has_error:
    print("\nFirst loop - inspection with break:")
    # First loop with break
    for i in range(start, stop + 1):
        if i == inspect:
            break
        print(i, end=" ")
    print()  # New line after first loop
    
    print("\nSecond loop - inspection with continue:")
    # Second loop with continue
    for i in range(start, stop + 1):
        if i == inspect:
            continue
        print(i, end=" ")
    print()  # New line after second loop

print("\nProgram ending.")