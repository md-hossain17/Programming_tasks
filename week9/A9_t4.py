TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius():
    """
    Collects Celsius temperature from user input.
    
    Returns:
        float: Valid Celsius temperature within range
        
    Raises:
        ValueError: If input cannot be converted to float
        Exception: If temperature is outside valid range
    """
    try:
        # Get user input
        user_input = input()
        
        # Try to convert to float
        celsius = float(user_input)
        
        # Check temperature range
        if celsius < TEMP_MIN or celsius > TEMP_MAX:
            raise Exception(f"{celsius} temperature out of range.")
        
        return celsius
        
    except ValueError:
        # Re-raise with the custom error message
        raise ValueError(f"could not convert string to float: '{user_input}'")

def main():
    """Main program to demonstrate collectCelsius function."""
    print("Temperature Collection Program")
    print(f"Valid range: {TEMP_MIN}°C to {TEMP_MAX}°C")
    print("Enter temperature in Celsius:")
    
    try:
        temperature = collectCelsius()
        print(f"Successfully collected temperature: {temperature}°C")
        
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()