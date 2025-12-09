def main():
    total = 0.0
    values = []
    
    print("=== Floating Point Sum Calculator ===")
    print("Enter values (0 to stop):")
    
    while True:
        try:
            # Get input
            raw_input = input("> ").strip()
            
            # Try to convert to float
            try:
                value = float(raw_input)
            except ValueError:
                print(f"Error: '{raw_input}' couldn't be converted to a floating-point number.")
                continue
            
            # Check for termination
            if value == 0:
                break
            
            # Display raw value
            print("Value: {}".format(raw_input))
            
            # Store and accumulate
            values.append(value)
            total += value
            
        except EOFError:
            print("\nEnd of input. Stopping.")
            break
        except KeyboardInterrupt:
            print("\n\nProgram interrupted.")
            break
    
    # Display summary
    if values:
        print(f"\nYou entered {len(values)} value(s).")
    else:
        print("\nNo valid values entered.")
    
    print("Sum: {:.2f}".format(total))

if __name__ == "__main__":
    main()