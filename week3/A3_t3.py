# Get username first
username = input("Enter your username: ")

# Display menu
print("\n--- Menu ---")
print("1. Print welcome message")
print("2. Exit")

while True:
    # Get user choice
    choice = input("\nYour choice: ")
    
    # Perform actions based on choice
    if choice == "1":
        print(f"Welcome {username}!")
    elif choice == "2":
        print("Exiting...")
        break
    else:
        print("Unknown option.")