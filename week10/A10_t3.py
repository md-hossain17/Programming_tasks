import sys

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if PAsc:
                if PValues[j] > PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
                    swapped = True
            else:
                if PValues[j] < PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
                    swapped = True
        if not swapped:
            break

def main() -> None:
    # Read filename
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = input()
    
    # Read numbers from file
    numbers = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                numbers.append(int(line))
    
    # Sort ascending
    asc_sorted = numbers.copy()
    bubbleSort(asc_sorted, PAsc=True)
    
    # Sort descending  
    desc_sorted = numbers.copy()
    bubbleSort(desc_sorted, PAsc=False)
    
    # Output both lists
    print(asc_sorted)
    print(desc_sorted)

if __name__ == "__main__":
    main()