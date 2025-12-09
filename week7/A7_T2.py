# main.py

def main():
    print("Program starting.")
    
    input_str = input("Insert comma separated integers: ").strip()
    
    if not input_str:
        print("No input provided.")
        print("Program ending.")
        return
    
    items = input_str.split(',')
    valid = []
    invalid = []
    
    for item in items:
        item = item.strip()
        if not item:
            continue
        try:
            valid.append(int(item))
        except:
            invalid.append(item)
    
    for bad in invalid:
        print(f"Error: '{bad}' is not a valid integer.")
    
    if not valid:
        print("No valid integers to analyze.")
    else:
        count = len(valid)
        total = sum(valid)
        parity = "even" if total % 2 == 0 else "odd"
        
        print(f"Total count of valid integers: {count}")
        print(f"Sum of valid integers: {total}")
        print(f"The sum is {parity}.")
    
    print("Program ending.")

if __name__ == "__main__":
    main()