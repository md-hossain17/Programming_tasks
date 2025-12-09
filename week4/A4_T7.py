print("Program starting.")
print()
print("Check multiplicative persistence.")
num = input("Insert an integer: ")

steps = 0
current = num

# Check if input is already a single digit
if len(current) == 1:
    print("No more steps.")
else:
    while True:
        # Convert current number to list of digits
        digits = [int(d) for d in str(current)]
        
        # Calculate product of digits
        product = 1
        for digit in digits:
            product *= digit
        
        # Format and print the current step
        if steps == 0:
            # First step: show the original input format
            equation = " * ".join(str(d) for d in digits)
            print(f"{equation} = {product}")
        else:
            # Subsequent steps
            equation = " * ".join(str(d) for d in digits)
            print(f"{equation} = {product}")
        
        steps += 1
        current = product
        
        # Stop if we reach a single digit
        if product < 10:
            print("No more steps.")
            break

print()
print(f"This program took {steps} step(s)")
print()
print("Program ending.")