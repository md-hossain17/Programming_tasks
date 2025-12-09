# main.py

def main():
    print("Program starting.")
    
    # Get filename
    filename = input("Insert the filename: ").strip()
    
    if not filename:
        print("No filename provided.")
        print("Program ending.")
        return
    
    # Read file
    data_rows = []
    try:
        with open(filename, 'r') as f:
            # Skip header
            next(f)
            
            for line in f:
                # Remove newline
                row = line.rstrip()
                
                # Skip empty lines
                if not row:
                    continue
                
                # Split by semicolon
                columns = row.split(';')
                data_rows.append(columns)
    except:
        print(f"Error reading file: {filename}")
        print("Program ending.")
        return
    
    if not data_rows:
        print("No data found.")
        print("Program ending.")
        return
    
    # Analyze per weekday
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", 
                "Friday", "Saturday", "Sunday"]
    results = []
    
    for weekday in weekdays:
        count = 0
        for row in data_rows:
            if row and row[0].startswith(weekday):
                count += 1
        results.append((weekday, count))
    
    # Display results
    print("\nTimestamp counts per weekday:")
    for weekday, count in results:
        print(f"{weekday}: {count}")
    
    total = sum(count for _, count in results)
    print(f"\nTotal timestamps: {total}")
    
    print("\nProgram ending.")

if __name__ == "__main__":
    main()