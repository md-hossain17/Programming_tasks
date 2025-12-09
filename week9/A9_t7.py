import sys
import os

def print_synopsis():
    """Print program usage instructions."""
    print("Usage: python {} <source_file> <destination_file>".format(sys.argv[0]))
    print("Copy the contents of source_file to destination_file")

def main():
    # Check argument count
    if len(sys.argv) != 3:
        print("Invalid amount of arguments.")
        print_synopsis()
        sys.exit(1)
    
    # Get source and destination filenames
    src_file = sys.argv[1]
    dst_file = sys.argv[2]
    
    # Check if destination file exists
    if os.path.exists(dst_file):
        # Prompt user for overwrite confirmation
        response = input(f"File '{dst_file}' already exists. Overwrite? (y/n): ").strip().lower()
        if response not in ['y', 'yes']:
            print("Operation cancelled.")
            sys.exit(0)
    
    try:
        # Read source file
        with open(src_file, 'r', encoding='utf-8') as src:
            content = src.read()
        
        # Write to destination file
        with open(dst_file, 'w', encoding='utf-8') as dst:
            dst.write(content)
        
        # Get file size for confirmation message
        file_size = os.path.getsize(src_file)
        print(f"Successfully copied '{src_file}' ({file_size} bytes) to '{dst_file}'")
        
    except FileNotFoundError:
        print(f"Error: Source file '{src_file}' not found.")
        sys.exit(-1)
    except PermissionError:
        print(f"Error: Permission denied for file '{src_file}' or '{dst_file}'.")
        sys.exit(-1)
    except IsADirectoryError:
        print(f"Error: '{src_file}' or '{dst_file}' is a directory, not a file.")
        sys.exit(-1)
    except UnicodeDecodeError:
        print(f"Error: Could not read '{src_file}' as text file (encoding issue).")
        sys.exit(-1)
    except Exception as e:
        print(f"Error: Unexpected error occurred: {e}")
        sys.exit(-1)

if __name__ == "__main__":
    main()