# main.py

def get_user_input() -> tuple:
    """
    Prompt user for first name, last name, and filename
    
    Returns:
        Tuple of (first_name, last_name, filename)
    """
    print("=== User Information Writer ===")
    print("Enter the following information:")
    
    # Get first name
    first_name = input("First name: ").strip()
    while not first_name:
        print("First name cannot be empty.")
        first_name = input("First name: ").strip()
    
    # Get last name
    last_name = input("Last name: ").strip()
    while not last_name:
        print("Last name cannot be empty.")
        last_name = input("Last name: ").strip()
    
    # Get filename
    filename = input("Filename to save (e.g., user_info.txt): ").strip()
    while not filename:
        print("Filename cannot be empty.")
        filename = input("Filename to save: ").strip()
    
    return first_name, last_name, filename

def write_to_file(filename: str, first_name: str, last_name: str) -> bool:
    """
    Write first name and last name to a text file
    
    Args:
        filename: Name of the file to write
        first_name: User's first name
        last_name: User's last name
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Write first name on first row
            file.write(first_name + '\n')
            # Write last name on second row
            file.write(last_name + '\n')
            # Add empty third row (just a newline)
            file.write('\n')
        
        print(f"\nFile '{filename}' created successfully!")
        return True
        
    except PermissionError:
        print(f"Error: No permission to write to '{filename}'")
        return False
    except Exception as e:
        print(f"Error writing file: {e}")
        return False

def display_preview(first_name: str, last_name: str, filename: str) -> None:
    """
    Show a preview of what will be written to the file
    
    Args:
        first_name: User's first name
        last_name: User's last name
        filename: Name of the file
    """
    print("\n" + "=" * 40)
    print("PREVIEW of file content:")
    print("=" * 40)
    print(f"File: {filename}")
    print("-" * 40)
    print(first_name)
    print(last_name)
    print("(empty line)")
    print("=" * 40)

def main() -> None:
    """
    Main program function
    """
    # Get user input
    first_name, last_name, filename = get_user_input()
    
    # Show preview
    display_preview(first_name, last_name, filename)
    
    # Confirm with user
    confirm = input("\nWrite to file? (y/n): ").strip().lower()
    
    if confirm == 'y':
        # Write to file
        success = write_to_file(filename, first_name, last_name)
        
        if success:
            # Show file content
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                print("\nFinal file content:")
                print("-" * 30)
                print(content)
                print("-" * 30)
            except:
                pass  # Just skip if we can't read it back
    else:
        print("Operation cancelled.")
    
    print("\nProgram completed. Goodbye!")

# Run the program
if __name__ == "__main__":
    main()