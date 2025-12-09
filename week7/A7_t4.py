import os
from dataclasses import dataclass
from typing import List

# Define a named datastructure for timestamp
@dataclass
class TIMESTAMP:
    weekday: str
    hour: int
    consumption: float  # in kWh
    price: float       # in €/kWh
    
    @property
    def total(self) -> float:
        """Calculate total cost for this timestamp"""
        return self.consumption * self.price

# Constants
DELIMITER = ";"

def readTimestamps(filename: str, timestamps_list: List[TIMESTAMP]) -> None:
    """
    Read timestamp data from CSV file and populate the list
    
    Args:
        filename: Path to the CSV file
        timestamps_list: List to store TIMESTAMP objects
    """
    try:
        with open(filename, 'r') as file:
            # Read file line by line
            for line in file:
                # Remove newline/whitespace from end
                row = line.rstrip()
                
                # Skip empty lines
                if not row:
                    continue
                
                # Skip header line (case-insensitive check)
                if row.lower().startswith("weekday"):
                    continue
                
                # Split the row by delimiter
                columns = row.split(DELIMITER)
                
                # Ensure we have exactly 4 columns
                if len(columns) != 4:
                    continue
                
                # Create TIMESTAMP object and assign values
                # Note: We need to handle possible conversion errors
                try:
                    weekday = columns[0].strip()
                    hour = int(columns[1].strip())
                    consumption = float(columns[2].strip())
                    price = float(columns[3].strip())
                    
                    # Create timestamp object
                    timestamp = TIMESTAMP(
                        weekday=weekday,
                        hour=hour,
                        consumption=consumption,
                        price=price
                    )
                    
                    # Add to list
                    timestamps_list.append(timestamp)
                    
                except ValueError as e:
                    print(f"Warning: Could not parse line: {row}")
                    print(f"Error: {e}")
                    continue
                    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")


def displayTimestamps(timestamps: List[TIMESTAMP]) -> None:
    """
    Display all timestamps with formatted output
    
    Args:
        timestamps: List of TIMESTAMP objects to display
    """
    if not timestamps:
        print("No timestamps to display.")
        return
    
    # Print header
    print("Timestamps:")
    
    # Initialize totals
    total_consumption = 0.0
    total_cost = 0.0
    
    # Display each timestamp
    for ts in timestamps:
        # Format as specified in test: starts with " - ", contains keywords
        # Example: " - Monday 8: price 0.15€/kWh, consumption 1.5kWh, total 0.225€"
        print(f" - {ts.weekday} {ts.hour}: price {ts.price}€/kWh, consumption {ts.consumption}kWh, total {ts.total:.3f}€")
        
        # Update totals
        total_consumption += ts.consumption
        total_cost += ts.total
    
    # Optional summary (test might not check this but it's good to have)
    # print(f"\nTotal consumption: {total_consumption:.2f}kWh")
    # print(f"Total cost: {total_cost:.2f}€")


# Main function for standalone execution
def main() -> None:
    """
    Main function to run the program
    """
    # Example: Read from a file (you can modify this as needed)
    filename = input("Enter the filename (e.g., A7_T4_D1.csv): ")
    
    # Create empty list for timestamps
    timestamps = []
    
    # Read timestamps from file
    readTimestamps(filename, timestamps)
    
    # Display timestamps if any were read
    if timestamps:
        displayTimestamps(timestamps)
    else:
        print("No data was read from the file.")


if __name__ == "__main__":
    # Run the main function
    main()