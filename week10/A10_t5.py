def recursiveFactorial(PNum: int) -> int:
    """
    Calculate factorial recursively.
    
    Args:
        PNum: Non-negative integer to calculate factorial for
        
    Returns:
        Factorial of PNum
        
    Raises:
        ValueError: If PNum is negative
        RecursionError: If recursion depth is too high
    """
    # Base case 1: Negative number
    if PNum < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base case 2: 0! = 1 and 1! = 1
    if PNum <= 1:
        return 1
    
    # Recursive case: n! = n * (n-1)!
    return PNum * recursiveFactorial(PNum - 1)

def main() -> None:
    """Main CLI program."""
    print("Factorial Calculator (Recursive)")
    print("=" * 30)
    
    while True:
        try:
            # Get user input
            user_input = input("\nEnter a non-negative integer (or 'q' to quit): ").strip()
            
            # Check for quit command
            if user_input.lower() in ['q', 'quit', 'exit']:
                print("Goodbye!")
                break
            
            # Try to convert to integer
            try:
                num = int(user_input)
            except ValueError:
                print("Please enter a valid integer.")
                continue
            
            # Calculate factorial
            try:
                result = recursiveFactorial(num)
                print(f"{num}! = {result}")
                
                # Show factorial calculation steps (optional)
                if num <= 10:  # Only show for small numbers
                    steps = [str(i) for i in range(num, 0, -1)]
                    print(f"Calculation: {' × '.join(steps)} = {result}")
                    
            except ValueError as ve:
                print(f"Error: {ve}")
            except RecursionError:
                print("Error: Recursion depth exceeded. Number too large for recursion.")
                print("Try a smaller number (Python's default recursion limit is ~1000).")
            
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break
        except EOFError:
            print("\n\nEnd of input. Goodbye!")
            break

# Alternative version with better error handling for recursion depth
def recursiveFactorialWithLimit(PNum: int, recursion_limit: int = 1000) -> int:
    """
    Calculate factorial recursively with safety check.
    
    Args:
        PNum: Non-negative integer
        recursion_limit: Maximum allowed recursion depth
        
    Returns:
        Factorial of PNum
    """
    if PNum < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Safety check to prevent excessive recursion
    if PNum > recursion_limit:
        raise RecursionError(f"Number exceeds safe recursion limit of {recursion_limit}")
    
    if PNum <= 1:
        return 1
    
    return PNum * recursiveFactorialWithLimit(PNum - 1, recursion_limit)

if __name__ == "__main__":
    # You can test the function directly
    print("Testing recursiveFactorial function:")
    test_cases = [0, 1, 2, 3, 4, 5, 10]
    for num in test_cases:
        try:
            result = recursiveFactorial(num)
            print(f"{num}! = {result}")
        except Exception as e:
            print(f"{num}! -> Error: {e}")
    
    # Run the main program
    main()