def showOptions():
    """Shows the available options and returns None"""
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askChoice():
    """Prompts user for choice and returns integer, handles invalid input"""
    choice = input("Your choice: ")
    
    # Check if input is numeric
    if not choice.isnumeric():
        print("Unknown option!")
        return -1  # Return -1 for invalid input
    
    return int(choice)

def main():
    """Main program logic with menu cycle"""
    count = 0
    
    while True:
        showOptions()
        choice = askChoice()
        print()
        
        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            print(f"Current count - {count}")
        elif choice == 2:
            count += 1
            print("Count increased!")
            print(f"Current count - {count}")
        elif choice == 3:
            count = 0
            print("Cleared count!")
            print(f"Current count - {count}")
        elif choice == -1:
            # Invalid input already handled in askChoice()
            pass
        else:
            print("Unknown option!")
        
        print()

# Start the program
print("Program starting.")
print()
main()
print()
print("Program ending.")