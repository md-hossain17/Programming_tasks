import sys

def main():
    # Get filename from user
    filename = input("Enter filename: ").strip()
    
    try:
        # Try to open and read the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Print the file content
        print("File content:")
        print("=" * 40)
        print(content)
        print("=" * 40)
        print(f"Successfully read file: {filename}")
        
    except FileNotFoundError:
        # Handle file not found error
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
        
    except PermissionError:
        # Handle permission errors
        print(f"Error: Permission denied to read '{filename}'.")
        sys.exit(1)
        
    except IsADirectoryError:
        # Handle if user entered a directory name
        print(f"Error: '{filename}' is a directory, not a file.")
        sys.exit(1)
        
    except UnicodeDecodeError:
        # Handle encoding issues
        print(f"Error: Could not decode '{filename}'. Try a different encoding.")
        sys.exit(1)
        
    except Exception as e:
        # Handle any other unexpected errors
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()