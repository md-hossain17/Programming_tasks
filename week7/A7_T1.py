# main.py

def collect_positive_integers() -> list:
    """
    Collect positive integers from user until negative number is entered
    
    Returns:
        List of positive integers collected
    """
    numbers = []
    print("\nEnter positive integers (negative number to stop):")
    
    while True:
        try:
            # Get user input
            user_input = input(f"Enter integer #{len(numbers) + 1}: ").strip()
            
            # Try to convert to integer
            num = int(user_input)
            
            # Check if negative (stop condition)
            if num < 0:
                print(f"Negative number ({num}) entered. Stopping input.")
                break
            
            # Check if positive (valid input)
            if num > 0:
                numbers.append(num)
                print(f"  Added: {num}")
            else:
                print(f"  Zero entered. Only positive integers are collected.")
                
        except ValueError:
            print(f"  Invalid input: '{user_input}'. Please enter an integer.")
    
    return numbers

def display_results(numbers: list) -> None:
    """
    Display collected integers with indices and ordinals
    
    Args:
        numbers: List of positive integers to display
    """
    if not numbers:
        print("\nNo positive integers were entered.")
        return
    
    print(f"\nCollected {len(numbers)} positive integer(s):")
    print("=" * 40)
    print(f"{'Index':<10} {'Ordinal':<10} {'Value':<10}")
    print("-" * 40)
    
    for i, num in enumerate(numbers):
        ordinal = i + 1
        print(f"{i:<10} {ordinal:<10} {num:<10}")
    
    print("=" * 40)
    
    # Additional statistics
    print(f"\nStatistics:")
    print(f"  Total count: {len(numbers)}")
    print(f"  Sum: {sum(numbers)}")
    print(f"  Average: {sum(numbers)/len(numbers):.2f}" if numbers else "  Average: N/A")
    print(f"  Maximum: {max(numbers)}" if numbers else "  Maximum: N/A")
    print(f"  Minimum: {min(numbers)}" if numbers else "  Minimum: N/A")

def main() -> None:
    """
    Main program function
    """
    print("Program starting.")
    print("This program collects positive integers.")
    
    # Collect positive integers
    numbers = collect_positive_integers()
    
    # Display results
    display_results(numbers)
    
    print("\nProgram ending.")

# Run the program
if __name__ == "__main__":
    main()