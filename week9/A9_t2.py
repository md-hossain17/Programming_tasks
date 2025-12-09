import sys

def main():
    print("=== Program Exit Code Setter ===")
    print("Enter an exit code between 0-255")
    print("(0 = success, 1-255 = error codes)")
    
    try:
        # Get user input
        user_input = input("> ").strip()
        
        # Try to convert to integer
        exit_code = int(user_input)
        
        # Check range (0-255 inclusive)
        if 0 <= exit_code <= 255:
            print(f"Exiting program with code: {exit_code}")
            sys.exit(exit_code)
        else:
            print(f"Error: {exit_code} is out of range (0-255)")
            sys.exit(1)  # Exit with general error
            
    except ValueError:
        print(f"Error: '{user_input}' is not a valid integer")
        sys.exit(1)
    except (KeyboardInterrupt, EOFError):
        print("\nExiting without setting code")
        sys.exit(1)

if __name__ == "__main__":
    main()