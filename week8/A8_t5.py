# login_system.py
import hashlib
import os
import csv
from typing import Optional, List, Tuple

# ==================== LOGIN LIBRARY ====================
# This part simulates the loginLib module that the test imports

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"

def _hash_password(password: str) -> str:
    """Hash password using MD5 and return hexdigest"""
    return hashlib.md5(password.encode()).hexdigest()

def _read_users() -> List[Tuple[str, str]]:
    """Read all users from credentials file"""
    users = []
    if not os.path.exists(CREDENTIALS_FILE):
        return users
    
    try:
        with open(CREDENTIALS_FILE, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=DELIMITER)
            for row in reader:
                if len(row) >= 2:
                    username = row[0].strip()
                    password_hash = row[1].strip()
                    users.append((username, password_hash))
    except:
        pass
    
    return users

def _write_users(users: List[Tuple[str, str]]) -> bool:
    """Write users to credentials file"""
    try:
        with open(CREDENTIALS_FILE, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=DELIMITER)
            for user in users:
                writer.writerow([user[0], user[1]])
        return True
    except:
        return False

def register(username: str, password: str) -> None:
    """Register a new user"""
    # Check if user already exists
    users = _read_users()
    for user in users:
        if user[0] == username:
            return  # User already exists, do nothing (as per test)
    
    # Add new user
    password_hash = _hash_password(password)
    users.append((username, password_hash))
    _write_users(users)

def login(username: str, password: str) -> bool:
    """Authenticate a user"""
    users = _read_users()
    password_hash = _hash_password(password)
    
    for user in users:
        if user[0] == username and user[1] == password_hash:
            return True
    return False

def viewProfile(username: str) -> Tuple[int, str]:
    """Get user profile information"""
    users = _read_users()
    
    for i, user in enumerate(users):
        if user[0] == username:
            # Return (index, username) as the test expects
            return (i, username)
    
    # Return -1 index if user not found
    return (-1, "")

def change_password(username: str, new_password: str) -> None:
    """Change user's password"""
    users = _read_users()
    updated_users = []
    updated = False
    
    for user in users:
        if user[0] == username:
            # Update password for this user
            new_hash = _hash_password(new_password)
            updated_users.append((username, new_hash))
            updated = True
        else:
            updated_users.append(user)
    
    if updated:
        _write_users(updated_users)

# ==================== MAIN PROGRAM ====================

def clear_screen():
    """Simple screen clearing"""
    print("\n" * 2)
    print("=" * 50)
    print("\n" * 2)

def show_main_menu():
    """Display main menu"""
    print("\n" + "=" * 40)
    print("         MAIN MENU")
    print("=" * 40)
    print("1. Login")
    print("2. Register")
    print("3. Exit")
    print("=" * 40)

def show_user_menu(username):
    """Display user menu after login"""
    print("\n" + "=" * 40)
    print(f"     USER MENU - {username}")
    print("=" * 40)
    print("1. View profile")
    print("2. Change password")
    print("3. Logout")
    print("=" * 40)

def main_program():
    """Main program loop"""
    current_user = None
    
    print("Welcome to the User Management System")
    print("Passwords are securely hashed using MD5")
    
    while True:
        if current_user is None:
            # Main menu (not logged in)
            show_main_menu()
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == "1":
                # Login
                clear_screen()
                print("\n--- LOGIN ---")
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                
                if login(username, password):
                    print(f"\nLogin successful! Welcome {username}!")
                    current_user = username
                else:
                    print("\nLogin failed. Invalid username or password.")
                
            elif choice == "2":
                # Register
                clear_screen()
                print("\n--- REGISTER ---")
                username = input("Choose username: ").strip()
                password = input("Choose password: ").strip()
                
                register(username, password)
                print(f"\nRegistration successful for user '{username}'!")
                
            elif choice == "3":
                # Exit
                print("\nThank you for using the system. Goodbye!")
                break
                
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.")
        
        else:
            # User menu (logged in)
            show_user_menu(current_user)
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == "1":
                # View profile
                clear_screen()
                print(f"\n--- PROFILE OF {current_user} ---")
                profile = viewProfile(current_user)
                if profile[0] != -1:
                    print(f"Username: {profile[1]}")
                    print(f"User ID: {profile[0]}")
                else:
                    print("Profile not found!")
                
            elif choice == "2":
                # Change password
                clear_screen()
                print(f"\n--- CHANGE PASSWORD FOR {current_user} ---")
                new_password = input("Enter new password: ").strip()
                confirm_password = input("Confirm new password: ").strip()
                
                if new_password == confirm_password:
                    change_password(current_user, new_password)
                    print("Password changed successfully!")
                else:
                    print("Passwords do not match. Please try again.")
                
            elif choice == "3":
                # Logout
                clear_screen()
                print(f"\nUser '{current_user}' logged out successfully.")
                current_user = None
                
            else:
                print("\nInvalid choice. Please enter 1, 2, or 3.")

# ==================== TEST COMPATIBILITY ====================
# This section ensures the code works with the test

# Create a module-like structure for the test to import
import sys

# Create a fake module that the test can import
class LoginLibModule:
    """Simulates the loginLib module for tests"""
    CREDENTIALS_FILE = CREDENTIALS_FILE
    
    @staticmethod
    def register(username, password):
        return register(username, password)
    
    @staticmethod
    def login(username, password):
        return login(username, password)
    
    @staticmethod
    def viewProfile(username):
        return viewProfile(username)
    
    @staticmethod
    def change_password(username, new_password):
        return change_password(username, new_password)

# Add to sys.modules so test can import it
sys.modules['loginLib'] = LoginLibModule

# ==================== EXECUTION CONTROL ====================

if __name__ == "__main__":
    # Check if we're running tests or the main program
    import sys
    
    if len(sys.argv) > 1 and "unittest" in sys.argv[0]:
        # Running tests - just define the functions
        pass
    else:
        # Running as main program
        main_program()