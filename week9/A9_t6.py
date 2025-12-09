import sys

def saveLines(lines):
    """Save lines to file."""
    filename = input()
    with open(filename, 'w', encoding='UTF-8') as f:
        f.writelines(lines)

def main():
    lines = []
    
    try:
        # Collect lines
        while True:
            line = input()
            lines.append(line + '\n')
            
    except KeyboardInterrupt:
        # Handle Ctrl+C
        if len(lines) == 0:
            print("No lines to save. Program closing.")
            sys.exit(0)
        else:
            # Ask if user wants to save
            try:
                answer = input("Do you want to save the lines to a file? (yes/no): ")
                if answer.lower() in ['yes', 'y']:
                    saveLines(lines)
            except (KeyboardInterrupt, EOFError):
                pass  # Exit without saving if interrupted again
                
    except EOFError:
        # Handle Ctrl+D (EOF)
        pass

if __name__ == "__main__":
    main()