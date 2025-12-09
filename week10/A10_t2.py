import sys

def readValues(PFilename: str, PValues: list[int]) -> None:
    """
    Read integers from a file, filtering empty rows and converting to integers.
    
    Args:
        PFilename: Name of the file to read
        PValues: List to store the integer values
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        ValueError: If a line cannot be converted to integer
    """
    try:
        with open(PFilename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, 1):
                # Strip whitespace and newline characters
                stripped_line = line.strip()
                
                # Skip empty lines
                if not stripped_line:
                    continue
                
                try:
                    # Convert to integer and add to list
                    value = int(stripped_line)
                    PValues.append(value)
                except ValueError:
                    print(f"Error on line {line_number}: '{stripped_line}' is not a valid integer")
                    sys.exit(1)
                    
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read '{PFilename}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def sumOfValues(PValues: list[int]) -> int:
    """
    Calculate the sum of all values in the list.
    
    Args:
        PValues: List of integers
        
    Returns:
        Sum of all values
    """
    return sum(PValues)

def productOfValues(PValues: list[int]) -> int:
    """
    Calculate the product of all values in the list.
    
    Args:
        PValues: List of integers
        
    Returns:
        Product of all values
    """
    if not PValues:
        return 0  # Or 1, depending on definition. Using 0 as safer default.
    
    product = 1
    for value in PValues:
        product *= value
    return product

def main() -> None:
    # 1. Initialize
    Values: list[int] = []
    
    # 2. Operate
    print("Program starting.")
    
    # 2.1 ask filename
    filename = input("Insert filename: ").strip()
    
    # 2.2 read values
    readValues(filename, Values)
    
    # Check if we got any values
    if not Values:
        print("No valid integer values found in the file.")
        # 3. Cleanup
        Values.clear()
        print("Program ending.")
        return None
    
    # 2.3 calculate sum of values
    total_sum = sumOfValues(Values)
    
    # 2.4 calculate product of values
    total_product = productOfValues(Values)
    
    # 2.5 display results
    print(f"\nAnalysis Results:")
    print(f"File analyzed: {filename}")
    print(f"Number of values: {len(Values)}")
    print(f"Sum of values: {total_sum}")
    print(f"Product of values: {total_product}")
    
    # Display all values (optional)
    if len(Values) <= 20:  # Only show if not too many values
        print(f"\nValues found: {Values}")
    
    # 3. Cleanup
    Values.clear()
    print("\nProgram ending.")
    return None

if __name__ == "__main__":
    main()