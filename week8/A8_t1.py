# main.py
import time

def main():
    duration = 1.0  # Default duration
    
    while True:
        print("\n--- Menu ---")
        print("1. Set pause duration")
        print("2. Activate pause")
        print("3. Exit")
        
        choice = input("Select: ")
        
        if choice == "1":
            try:
                duration = float(input("Seconds: "))
                print(f"Set to {duration}s")
            except:
                print("Invalid number")
        
        elif choice == "2":
            print(f"Pausing for {duration} seconds...")
            time.sleep(duration)
            print("Done!")
        
        elif choice == "3":
            print("Bye!")
            break
        
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()