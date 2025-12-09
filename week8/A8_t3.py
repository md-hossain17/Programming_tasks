# main.py

def show_menu() -> None:
    """
    Display the main menu options
    """
    print("\n" + "=" * 40)
    print("NUMBER FILE ANALYZER")
    print("=" * 40)
    print("1. Read values from file")
    print("2. Show amount of values")
    print("3. Calculate sum of values")
    print("4. Calculate average of values")
    print("5. Show all statistics")
    print("6. Exit")
    print("=" * 40)

def get_choice() -> int:
    """
    Get user's menu choice
    
    Returns:
        Integer choice (1-6)
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-6): "))
            if 1 <= choice <= 6:
                return choice
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def read_values() -> list:
    """
    Read values from a file and convert to floats
    
    Returns:
        List of float values
    """
    filename = input("Enter filename (e.g., A8_T3_D1.txt): ").strip()
    
    if not filename:
        print("No filename provided.")
        return []
    
    values = []
    
    try:
        with open(filename, 'r') as file:
            for line_num, line in enumerate(file, 1):
                # Remove whitespace and newline characters
                line = line.strip()
                
                # Skip empty lines
                if not line:
                    continue
                
                try:
                    # Convert to float and add to list
                    value = float(line)
                    values.append(value)
                except ValueError:
                    print(f"Warning: Line {line_num} contains non-numeric value: '{line}'")
        
        print(f"Successfully read {len(values)} values from '{filename}'.")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    return values

def show_amount(values: list) -> None:
    """
    Display the amount of values in the list
    
    Args:
        values: List of float values
    """
    if not values:
        print("No values loaded. Please read values from a file first.")
        return
    
    count = len(values)
    print(f"Amount of values: {count}")

def calculate_sum(values: list) -> float:
    """
    Calculate the sum of values
    
    Args:
        values: List of float values
        
    Returns:
        Sum of values rounded to 1 decimal place
    """
    if not values:
        return 0.0
    
    total = sum(values)
    return round(total, 1)

def calculate_average(values: list) -> float:
    """
    Calculate the average of values
    
    Args:
        values: List of float values
        
    Returns:
        Average of values rounded to 1 decimal place
    """
    if not values:
        return 0.0
    
    total = sum(values)
    count = len(values)
    average = total / count if count > 0 else 0.0
    return round(average, 1)

def show_sum(values: list) -> None:
    """
    Display the sum of values
    
    Args:
        values: List of float values
    """
    if not values:
        print("No values loaded. Please read values from a file first.")
        return
    
    total = calculate_sum(values)
    print(f"Sum of values: {total}")

def show_average(values: list) -> None:
    """
    Display the average of values
    
    Args:
        values: List of float values
    """
    if not values:
        print("No values loaded. Please read values from a file first.")
        return
    
    average = calculate_average(values)
    print(f"Average of values: {average}")

def show_all_statistics(values: list) -> None:
    """
    Display all statistics at once
    
    Args:
        values: List of float values
    """
    if not values:
        print("No values loaded. Please read values from a file first.")
        return
    
    print("\n" + "=" * 40)
    print("STATISTICS SUMMARY")
    print("=" * 40)
    
    # Amount
    count = len(values)
    print(f"Amount of values: {count}")
    
    # Sum
    total = calculate_sum(values)
    print(f"Sum of values: {total}")
    
    # Average
    average = calculate_average(values)
    print(f"Average of values: {average}")
    
    # Additional statistics
    if values:
        min_val = min(values)
        max_val = max(values)
        print(f"Minimum value: {min_val:.1f}")
        print(f"Maximum value: {max_val:.1f}")
    
    print("=" * 40)

def main() -> None:
    """
    Main program function
    """
    print("Welcome to the Number File Analyzer")
    print("This program analyzes numeric data from text files.")
    print("Available datasets: A8_T3_D1.txt, A8_T3_D2.txt")
    
    values = []  # Initialize empty list for values
    
    while True:
        show_menu()
        choice = get_choice()
        
        if choice == 1:
            # Read values from file
            values = read_values()
            
        elif choice == 2:
            # Show amount of values
            show_amount(values)
            
        elif choice == 3:
            # Calculate and show sum
            show_sum(values)
            
        elif choice == 4:
            # Calculate and show average
            show_average(values)
            
        elif choice == 5:
            # Show all statistics
            show_all_statistics(values)
            
        elif choice == 6:
            # Exit program
            print("\nThank you for using the Number File Analyzer!")
            print("Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()