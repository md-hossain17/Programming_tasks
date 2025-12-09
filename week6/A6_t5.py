# main.py

def readValues(filename: str) -> list:
    """
    Read numbers from a text file
    
    Args:
        filename: Path to the text file
        
    Returns:
        List of integers read from the file
    """
    numbers = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Check if line is not empty
                    try:
                        # Convert to integer and add to list
                        number = int(line)
                        numbers.append(number)
                    except ValueError:
                        # Skip lines that can't be converted to integers
                        continue
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    return numbers


def analyseValues(values: list) -> str:
    """
    Analyze a list of numbers and return formatted results
    
    Args:
        values: List of numbers to analyze
        
    Returns:
        Formatted string with headers and results in CSV format
    """
    if not values:
        # Return empty results if no values
        return "Count;Sum;Greatest;Average\n0;0;0;0.00\n"
    
    # Calculate statistics
    count = len(values)
    total_sum = sum(values)
    greatest = max(values)
    average = total_sum / count if count > 0 else 0
    
    # Format the results exactly as required
    headers = "Count;Sum;Greatest;Average"
    data_row = f"{count};{total_sum};{greatest};{average:.2f}"
    
    return f"{headers}\n{data_row}\n"


def displayResults(results: str) -> None:
    """
    Display the analysis results
    
    Args:
        results: Formatted string with analysis results
    """
    print(results)


def main() -> None:
    """
    Main program function
    """
    # Get filename from user
    filename = input("Enter the filename to analyze: ").strip()
    
    # Read values from file
    values = readValues(filename)
    
    if not values:
        print("No valid numbers found in the file.")
        return
    
    # Analyze the values
    results = analyseValues(values)
    
    # Display the results
    displayResults(results)


# Alternative simpler version if needed for testing
def simple_readValues(filename: str) -> list:
    """Simpler version for testing"""
    numbers = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    numbers.append(int(line))
    except:
        pass
    return numbers


def simple_analyseValues(values: list) -> str:
    """Simpler version for testing"""
    count = len(values)
    total = sum(values)
    greatest = max(values) if values else 0
    average = total / count if count > 0 else 0
    
    return f"Count;Sum;Greatest;Average\n{count};{total};{greatest};{average:.2f}\n"


# For direct execution
if __name__ == "__main__":
    main()