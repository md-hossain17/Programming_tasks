# main.py

def readFile(filename: str) -> str:
    """
    Read the entire content of a file
    
    Args:
        filename: A6_T1_D1.txt
        
    Returns:
        Content of the file as a string, or empty string if file not found
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

def printWithDecoration(filename: str, content: str) -> None:
    """
    Print file content with decorative headers and footers
    
    Args:
        filename: Name of the file (for decoration)
        content: Content of the file to print
    """
    # Create decorative lines
    start_line = f"#### START \"{filename}\" ####"
    end_line = f"#### END \"{filename}\" ####"
    
    # Print everything
    print(start_line)
    print(content.rstrip())  # rstrip to remove trailing newlines
    print(end_line)

def main() -> None:
    """
    Main program: Ask for filename, read file, print with decoration
    """
    print("File Reader with Decoration")
    print("=" * 40)
    
    # Get filename from user
    filename = input("Enter the filename to read: ").strip()
    
    if not filename:
        print("No filename provided. Exiting.")
        return
    
    # Read file content
    content = readFile(filename)
    
    # Check if we got content
    if content is not None:
        # Print with decoration
        print("\n" + "=" * 40)
        printWithDecoration(filename, content)
        print("=" * 40)
    else:
        print("Failed to read file content.")

# Run if executed directly
if __name__ == "__main__":
    main()