import sys

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    """
    Merge two sorted lists into PMerge list.
    
    Args:
        PLeft: Sorted left list
        PRight: Sorted right list
        PMerge: List to store merged result (will be modified in-place)
        PAsc: If True, merge in ascending order; if False, descending order
    """
    # Clear PMerge first
    PMerge.clear()
    
    i = 0  # Index for PLeft
    j = 0  # Index for PRight
    
    # Compare and merge elements from both lists
    while i < len(PLeft) and j < len(PRight):
        if PAsc:
            # Ascending order: take smaller element first
            if PLeft[i] <= PRight[j]:
                PMerge.append(PLeft[i])
                i += 1
            else:
                PMerge.append(PRight[j])
                j += 1
        else:
            # Descending order: take larger element first
            if PLeft[i] >= PRight[j]:
                PMerge.append(PLeft[i])
                i += 1
            else:
                PMerge.append(PRight[j])
                j += 1
    
    # Append any remaining elements from left list
    while i < len(PLeft):
        PMerge.append(PLeft[i])
        i += 1
    
    # Append any remaining elements from right list
    while j < len(PRight):
        PMerge.append(PRight[j])
        j += 1

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    """
    Sort PValues in-place using merge sort algorithm.
    
    Args:
        PValues: List of integers to sort
        PAsc: If True, sort ascending; if False, sort descending
    """
    # Base case: list with 0 or 1 element is already sorted
    if len(PValues) <= 1:
        return
    
    # Divide: find the middle point
    mid = len(PValues) // 2
    
    # Conquer: recursively sort left and right halves
    left = PValues[:mid]  # Copy left half
    right = PValues[mid:]  # Copy right half
    
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)
    
    # Combine: merge the sorted halves back into PValues
    # Clear PValues and merge left and right into it
    merged = []
    merge(left, right, merged, PAsc)
    
    # Copy merged result back to PValues
    PValues[:] = merged

def read_numbers_from_file(filename: str) -> list[int]:
    """
    Read integers from a file, ignoring empty lines and non-integer values.
    
    Args:
        filename: Name of the file to read
        
    Returns:
        List of integers read from the file
    """
    numbers = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                stripped_line = line.strip()
                
                # Skip empty lines
                if not stripped_line:
                    continue
                
                try:
                    # Convert to integer
                    number = int(stripped_line)
                    numbers.append(number)
                except ValueError:
                    # Skip non-integer values silently
                    continue
        
        return numbers
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        sys.exit(1)

def main() -> None:
    """Main program entry point."""
    # Determine the filename
    filename = ""
    
    if len(sys.argv) == 2:
        # Use command line argument (sys.argv[1])
        filename = sys.argv[1]
        print(f"Using command line argument: {filename}")
    elif len(sys.argv) == 1:
        # No command line arguments, prompt user
        filename = input("Enter filename: ").strip()
        if not filename:
            print("No filename provided. Exiting.")
            sys.exit(1)
    else:
        # Too many arguments
        print("Usage: python A10_T4.py [filename]")
        print("If no filename is provided, you will be prompted for one.")
        sys.exit(1)
    
    # Read numbers from file
    original_numbers = read_numbers_from_file(filename)
    
    if not original_numbers:
        print("No valid integers found in the file.")
        print("Program ending.")
        return
    
    print(f"Successfully read {len(original_numbers)} integer(s).")
    print(f"Original numbers: {original_numbers}")
    
    # Create copies for sorting (original list should not be modified)
    asc_numbers = original_numbers.copy()
    desc_numbers = original_numbers.copy()
    
    # Sort in ascending order (default)
    mergeSort(asc_numbers, PAsc=True)
    
    # Sort in descending order
    mergeSort(desc_numbers, PAsc=False)
    
    # Display results
    print(f"\nAscending sorted: {asc_numbers}")
    print(f"Descending sorted: {desc_numbers}")

if __name__ == "__main__":
    main()