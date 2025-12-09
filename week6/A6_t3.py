# main.py

def read_source_file(filename: str) -> str:
    """
    Read content from source file
    
    Args:
        filename: Source file to read from
        
    Returns:
        Content of the file as string, or None if error occurs
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: Source file '{filename}' not found.")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def write_destination_file(filename: str, content: str) -> bool:
    """
    Write content to destination file
    
    Args:
        filename: Destination file to write to
        content: Content to write
        
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except PermissionError:
        print(f"Error: No permission to write to '{filename}'.")
        return False
    except Exception as e:
        print(f"Error writing file: {e}")
        return False

def copy_file(source: str, destination: str) -> bool:
    """
    Copy content from source file to destination file
    
    Args:
        source: Source filename
        destination: Destination filename
        
    Returns:
        True if copy successful, False otherwise
    """
    # Read source file
    print(f"Reading file '{source}' content.")
    content = read_source_file(source)
    
    if content is None:
        return False
    
    print("File content ready in memory.")
    
    # Write to destination file
    print(f"Writing content into file '{destination}'.")
    
    if write_destination_file(destination, content):
        print("Copying operation complete.")
        return True
    else:
        return False

def main() -> None:
    """
    Main program function
    """
    print("Program starting.")
    print("This program can copy a file.")
    
    # Get source filename
    source = input("Insert source filename: ").strip()
    if not source:
        print("No source filename provided. Exiting.")
        print("Program ending.")
        return
    
    # Get destination filename
    destination = input("Insert destination filename: ").strip()
    if not destination:
        print("No destination filename provided. Exiting.")
        print("Program ending.")
        return
    
    # Check if source and destination are the same
    if source == destination:
        print("Error: Source and destination files cannot be the same.")
        print("Program ending.")
        return
    
    # Perform copy operation
    success = copy_file(source, destination)
    
    if success:
        print("Copy completed successfully.")
    else:
        print("Copy failed.")
    
    print("Program ending.")

# Run the program
if __name__ == "__main__":
    main()