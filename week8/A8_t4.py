# main.py
import timestamp_lib
from datetime import datetime
from typing import List

def show_menu() -> None:
    """
    Display the main menu
    """
    print("\n" + "=" * 50)
    print("TIMESTAMP ANALYZER")
    print("=" * 50)
    print("1. Read timestamps from file")
    print("2. Show loaded timestamp information")
    print("3. Count timestamps by year")
    print("4. Count timestamps by month")
    print("5. Count timestamps by weekday")
    print("6. Show all statistics")
    print("7. Clear loaded timestamps")
    print("8. Exit")
    print("=" * 50)

def get_choice() -> int:
    """
    Get user's menu choice
    
    Returns:
        Integer choice (1-8)
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-8): "))
            if 1 <= choice <= 8:
                return choice
            else:
                print("Please enter a number between 1 and 8.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_filename() -> str:
    """
    Get filename from user
    
    Returns:
        Filename as string
    """
    filename = input("Enter filename (e.g., A8_T4_D1.txt): ").strip()
    return filename

def get_year() -> int:
    """
    Get year from user
    
    Returns:
        Year as integer
    """
    while True:
        try:
            year = int(input("Enter year (e.g., 2023): "))
            if 1000 <= year <= 9999:  # Reasonable year range
                return year
            else:
                print("Please enter a valid 4-digit year.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_month() -> str:
    """
    Get month name from user
    
    Returns:
        Month name as string
    """
    print("\nAvailable months:")
    for i, month in enumerate(timestamp_lib.MONTHS, 1):
        print(f"  {i:2}. {month}")
    
    while True:
        month_input = input("\nEnter month name or number (1-12): ").strip()
        
        # Check if input is a number
        if month_input.isdigit():
            month_num = int(month_input)
            if 1 <= month_num <= 12:
                return timestamp_lib.MONTHS[month_num - 1]
            else:
                print("Please enter a number between 1 and 12.")
        else:
            # Check if input is a month name
            if month_input in timestamp_lib.MONTHS:
                return month_input
            else:
                print(f"'{month_input}' is not a valid month name.")

def get_weekday() -> str:
    """
    Get weekday name from user
    
    Returns:
        Weekday name as string
    """
    print("\nAvailable weekdays:")
    for i, weekday in enumerate(timestamp_lib.WEEKDAYS, 1):
        print(f"  {i}. {weekday}")
    
    while True:
        weekday_input = input("\nEnter weekday name: ").strip()
        
        if weekday_input in timestamp_lib.WEEKDAYS:
            return weekday_input
        else:
            print(f"'{weekday_input}' is not a valid weekday name.")

def show_all_statistics(timestamps: List[datetime]) -> None:
    """
    Display all statistics for loaded timestamps
    
    Args:
        timestamps: List of datetime objects
    """
    if not timestamps:
        print("No timestamps loaded.")
        return
    
    print("\n" + "=" * 60)
    print("TIMESTAMP STATISTICS")
    print("=" * 60)
    
    # Show basic info
    timestamp_lib.getTimestampInfo(timestamps)
    print("-" * 60)
    
    # Count by year
    years = timestamp_lib.getAvailableYears(timestamps)
    print("\nCount by Year:")
    for year in years:
        count = timestamp_lib.calculateYears(year, timestamps)
        print(f"  {year}: {count} timestamps")
    
    # Count by month
    print("\nCount by Month:")
    for month in timestamp_lib.MONTHS:
        count = timestamp_lib.calculateMonths(month, timestamps)
        if count > 0:  # Only show months with data
            print(f"  {month}: {count} timestamps")
    
    # Count by weekday
    print("\nCount by Weekday:")
    for weekday in timestamp_lib.WEEKDAYS:
        count = timestamp_lib.calculateWeekdays(weekday, timestamps)
        print(f"  {weekday}: {count} timestamps")
    
    print("=" * 60)

def main() -> None:
    """
    Main program function
    """
    print("Welcome to the Timestamp Analyzer")
    print("This program analyzes timestamps from text files.")
    print("Available datasets: A8_T4_D1.txt, A8_T4_D2.txt")
    
    # Initialize empty list for timestamps
    timestamps: List[datetime] = []
    
    while True:
        show_menu()
        choice = get_choice()
        
        if choice == 1:
            # Read timestamps from file
            filename = get_filename()
            if filename:
                # Clear existing timestamps or append?
                clear_choice = input("Clear existing timestamps? (y/n): ").strip().lower()
                if clear_choice == 'y':
                    timestamps.clear()
                timestamp_lib.readTimestamps(filename, timestamps)
        
        elif choice == 2:
            # Show loaded timestamp information
            timestamp_lib.getTimestampInfo(timestamps)
        
        elif choice == 3:
            # Count timestamps by year
            if not timestamps:
                print("No timestamps loaded. Please read a file first.")
                continue
            
            year = get_year()
            count = timestamp_lib.calculateYears(year, timestamps)
            print(f"\nTimestamps in year {year}: {count}")
        
        elif choice == 4:
            # Count timestamps by month
            if not timestamps:
                print("No timestamps loaded. Please read a file first.")
                continue
            
            month = get_month()
            count = timestamp_lib.calculateMonths(month, timestamps)
            print(f"\nTimestamps in {month}: {count}")
        
        elif choice == 5:
            # Count timestamps by weekday
            if not timestamps:
                print("No timestamps loaded. Please read a file first.")
                continue
            
            weekday = get_weekday()
            count = timestamp_lib.calculateWeekdays(weekday, timestamps)
            print(f"\nTimestamps on {weekday}: {count}")
        
        elif choice == 6:
            # Show all statistics
            show_all_statistics(timestamps)
        
        elif choice == 7:
            # Clear loaded timestamps
            timestamps.clear()
            print("All timestamps cleared.")
        
        elif choice == 8:
            # Exit program
            print("\nThank you for using the Timestamp Analyzer!")
            print("Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()