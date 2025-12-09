import os
from typing import List, Tuple
from collections import defaultdict

# Constants
DELIMITER = ";"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Data structures
class TIMESTAMP:
    """Represents a single timestamp record"""
    def __init__(self, weekday: str, hour: int, consumption: float, price: float):
        self.weekday = weekday
        self.hour = hour
        self.consumption = consumption  # kWh
        self.price = price  # €/kWh
    
    @property
    def cost(self) -> float:
        """Calculate cost for this timestamp"""
        return self.consumption * self.price


class DAY_USAGE:
    """Helper structure for daily analysis"""
    def __init__(self, weekday: str):
        self.weekday = weekday
        self.total_consumption = 0.0  # kWh
        self.total_cost = 0.0  # €


def readTimestamps(filename: str) -> List[TIMESTAMP]:
    """
    Read timestamps from CSV file
    
    Args:
        filename: Path to CSV file
        
    Returns:
        List of TIMESTAMP objects
    """
    timestamps: List[TIMESTAMP] = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove newline and whitespace
                row = line.rstrip()
                
                # Skip empty lines and header
                if not row or row.lower().startswith("weekday"):
                    continue
                
                # Split by delimiter
                columns = row.split(DELIMITER)
                
                # Ensure we have exactly 4 columns
                if len(columns) != 4:
                    continue
                
                try:
                    # Parse columns
                    weekday = columns[0].strip()
                    hour = int(columns[1].strip())
                    consumption = float(columns[2].strip())
                    price = float(columns[3].strip())
                    
                    # Create timestamp object
                    timestamp = TIMESTAMP(weekday, hour, consumption, price)
                    timestamps.append(timestamp)
                    
                except ValueError:
                    # Skip lines that can't be parsed
                    continue
                    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    return timestamps


def analyzeDailyUsage(timestamps: List[TIMESTAMP]) -> List[DAY_USAGE]:
    """
    Analyze timestamps and calculate daily usage and cost
    
    Args:
        timestamps: List of TIMESTAMP objects
        
    Returns:
        List of DAY_USAGE objects for each weekday in order
    """
    # Create DAY_USAGE objects for all weekdays
    daily_usage = {day: DAY_USAGE(day) for day in WEEKDAYS}
    
    # Process each timestamp
    for ts in timestamps:
        if ts.weekday in daily_usage:
            day = daily_usage[ts.weekday]
            day.total_consumption += ts.consumption  # Gatherer for daily usage
            day.total_cost += ts.cost  # Gatherer for daily cost
    
    # Return in weekday order
    return [daily_usage[day] for day in WEEKDAYS]


def createSummary(daily_usage: List[DAY_USAGE]) -> List[str]:
    """
    Create formatted summary strings from daily usage analysis
    
    Args:
        daily_usage: List of DAY_USAGE objects
        
    Returns:
        List of formatted summary strings
    """
    results: List[str] = []
    
    for day_usage in daily_usage:
        # Handle the "Saturnday" typo if needed
        display_day = "Saturnday" if day_usage.weekday == "Saturday" else day_usage.weekday
        
        # Format: " - Monday usage 2510.00 kWh, cost 279.42 €"
        summary_line = f" - {display_day} usage {day_usage.total_consumption:.2f} kWh, cost {day_usage.total_cost:.2f} €"
        results.append(summary_line)
    
    return results


def displayResults(summary_lines: List[str]) -> None:
    """
    Display the formatted results
    
    Args:
        summary_lines: List of formatted summary strings
    """
    print("### Electricity consumption summary ###")
    for line in summary_lines:
        print(line)
    print("### Electricity consumption summary ###")


def main() -> None:
    """Main program entry point"""
    print("Program starting.")
    
    # Get filename from user
    filename = input("Enter filename: ")
    print(f'Reading file "{filename}".')
    
    print("Analysing timestamps.")
    
    # Read timestamps from file
    timestamps = readTimestamps(filename)
    
    if not timestamps:
        print("No valid timestamps found in the file.")
        print("Program ending.")
        return
    
    print("Displaying results.")
    
    # Analyze daily usage
    daily_usage = analyzeDailyUsage(timestamps)
    
    # Create summary
    summary_lines = createSummary(daily_usage)
    
    # Display results
    displayResults(summary_lines)
    
    print("Program ending.")


if __name__ == "__main__":
    main()