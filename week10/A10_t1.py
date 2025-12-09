import os

def read_file_content(filename):
    """
    Read file and return non-empty lines as a list.
    Strips newlines and ignores empty lines.
    """
    lines = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Strip newline characters and whitespace
                stripped_line = line.strip()
                
                # Only add non-empty lines
                if stripped_line:
                    lines.append(stripped_line)
                    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
    return lines

def display_content_vertically(lines):
    """Display each value on its own row."""
    print("\nVertical display:")
    print("-" * 30)
    for line in lines:
        print(line)
    print("-" * 30)

def display_content_horizontally(lines):
    """Display all values on the same row, separated by ', '."""
    print("\nHorizontal display:")
    print("-" * 30)
    if lines:
        print(", ".join(lines))
    print("-" * 30)

def main():
    print("=== File Content Display Program ===")
    
    # Get filename from user
    filename = input("Insert filename: ").strip()
    
    # Read file content
    lines = read_file_content(filename)
    
    # If file reading failed, exit
    if lines is None:
        return
    
    # If file is empty, inform user
    if not lines:
        print(f"File '{filename}' is empty or contains only empty lines.")
        return
    
    # Display statistics
    print(f"\nFile: {filename}")
    print(f"Non-empty lines: {len(lines)}")
    
    # Display content vertically
    display_content_vertically(lines)
    
    # Display content horizontally  
    display_content_horizontally(lines)

if __name__ == "__main__":
    main()