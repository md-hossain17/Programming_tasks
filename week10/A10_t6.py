import sys
import time
import copy
from typing import Callable

def readValues(PValues: list[int]) -> None:
    """Read dataset values from user-selected file."""
    PValues.clear()  # Clear existing values
    
    # Available datasets
    datasets = {
        '1': 'A10_D10.txt',
        '2': 'A10_D100.txt', 
        '3': 'A10_D1000.txt'
    }
    
    print("\nAvailable datasets:")
    print("1. A10_D10.txt (10 values)")
    print("2. A10_D100.txt (100 values)")
    print("3. A10_D1000.txt (1000 values)")
    
    choice = input("Select dataset (1-3): ").strip()
    
    if choice not in datasets:
        print("Invalid selection.")
        return
    
    filename = datasets[choice]
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        PValues.append(int(line))
                    except ValueError:
                        print(f"Warning: Skipping non-integer value: '{line}'")
        
        print(f"Successfully read {len(PValues)} values from {filename}")
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        print("Make sure the dataset files are in the same directory.")
    except Exception as e:
        print(f"Error reading file: {e}")

def bubbleSort(PNums: list[int]) -> list[int]:
    """Bubble sort implementation."""
    nums = PNums.copy()  # Work on a copy
    n = len(nums)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    
    return nums

def quickSort(PNums: list[int]) -> list[int]:
    """Quick sort implementation."""
    if len(PNums) <= 1:
        return PNums.copy()
    
    pivot = PNums[len(PNums) // 2]
    left = [x for x in PNums if x < pivot]
    middle = [x for x in PNums if x == pivot]
    right = [x for x in PNums if x > pivot]
    
    return quickSort(left) + middle + quickSort(right)

def measureSortingTime(PSortingAlgorithm: Callable, PArr: list[int]) -> int:
    """Measure sorting time in nanoseconds."""
    # Create a deep copy to ensure original isn't modified
    arr_copy = copy.deepcopy(PArr)
    
    # Measure time
    start_time = time.perf_counter_ns()
    result = PSortingAlgorithm(arr_copy)
    end_time = time.perf_counter_ns()
    
    # Verify sorting worked (optional but good for debugging)
    if result != sorted(PArr):
        print("Warning: Sorting algorithm may not be working correctly")
    
    return end_time - start_time

def measureSpeeds(PValues: list[int], PResults: list[str]) -> None:
    """Measure and compare sorting speeds."""
    if not PValues:
        print("No data loaded. Please read dataset first (Option 1).")
        return
    
    print("\n" + "="*50)
    print("MEASURING SORTING SPEEDS")
    print("="*50)
    print(f"Dataset size: {len(PValues)} values")
    
    # Clear previous results
    PResults.clear()
    
    # Measure Built-in sorted
    print("\nMeasuring Built-in sorted...")
    builtin_time = measureSortingTime(sorted, PValues)
    PResults.append(f"Built-in sorted: {builtin_time:,} ns")
    print(f"  Built-in sorted: {builtin_time:,} nanoseconds")
    
    # Measure Bubble sort
    print("Measuring Bubble sort...")
    bubble_time = measureSortingTime(bubbleSort, PValues)
    PResults.append(f"Bubble sort: {bubble_time:,} ns")
    print(f"  Bubble sort: {bubble_time:,} nanoseconds")
    
    # Measure Quick sort
    print("Measuring Quick sort...")
    quick_time = measureSortingTime(quickSort, PValues)
    PResults.append(f"Quick sort: {quick_time:,} ns")
    print(f"  Quick sort: {quick_time:,} nanoseconds")
    
    # Calculate ratios
    if builtin_time > 0:
        bubble_ratio = bubble_time / builtin_time
        quick_ratio = quick_time / builtin_time
        print(f"\nPerformance ratios (relative to built-in sorted):")
        print(f"  Bubble sort: {bubble_ratio:.1f}x slower")
        print(f"  Quick sort: {quick_ratio:.1f}x slower")
    
    print("="*50)

def saveResults(PResults: list[str]) -> None:
    """Save timing results to a file."""
    if not PResults:
        print("No results to save. Please measure speeds first (Option 2).")
        return
    
    filename = input("Enter filename to save results: ").strip()
    if not filename:
        print("No filename provided.")
        return
    
    # Add .txt extension if not present
    if not filename.lower().endswith('.txt'):
        filename += '.txt'
    
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("Sorting Algorithm Performance Results\n")
            file.write("="*40 + "\n")
            for result in PResults:
                file.write(result + "\n")
        print(f"Results saved to '{filename}'")
    except Exception as e:
        print(f"Error saving file: {e}")

def print_menu() -> None:
    """Print the main menu."""
    print("\n" + "="*40)
    print("SORTING ALGORITHM PERFORMANCE ANALYZER")
    print("="*40)
    print("1. Read dataset values")
    print("2. Measure sorting speeds")
    print("3. Save results to file")
    print("0. Exit")
    print("-"*40)

def main() -> None:
    """Main program."""
    # 1. Initialize
    Values: list[int] = []
    Results: list[str] = []
    
    # 2. Operate
    print("Program starting.")
    
    while True:
        print_menu()
        
        try:
            choice = input("Enter your choice (0-3): ").strip()
            
            if choice == '0':
                print("\nExiting program. Goodbye!")
                break
                
            elif choice == '1':
                readValues(Values)
                
            elif choice == '2':
                measureSpeeds(Values, Results)
                
            elif choice == '3':
                saveResults(Results)
                
            else:
                print("Invalid choice. Please enter 0, 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")
    
    # 3. Cleanup
    Values.clear()
    Results.clear()
    print("\nProgram ending.")

if __name__ == "__main__":
    main()