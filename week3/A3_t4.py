# Get username first
username = input("Enter your username: ")

# Display menu
print("\n--- Menu ---")
print("1. Print welcome message")
print("2. Print the name backwards")
print("3. Print the first character")
print("4. Show the amount of characters in the name")
print("5. Exit")

while True:
    # Get user choice
    choice = input("\nYour choice: ")
    
    # Perform actions based on choice
    if choice == "1":
        print(f"Welcome {username}!")
    elif choice == "2":
        name_backwards = username[::-1]
        print(f'Your name backwards is "{name_backwards}"')
    elif choice == "3":
        if username:  # Check if name is not empty
            first_char = username[0]
            print(f'The first character in name "{username}" is "{first_char}"')
        else:
            print("Name is empty!")
    elif choice == "4":
        name_length = len(username)
        print(f'There are {name_length} characters in the name "{username}"')
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Unknown option.")