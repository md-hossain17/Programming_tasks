def multi_branched_decision(num):
    """Using one multi-branched decision (if-elif-else)."""
    if num < 100:
        result = num + 10
    elif num < 200:
        result = num + 20
    elif num < 300:
        result = num + 22
    else:
        result = num + 25
    return result


def multiple_independent_ifs(num):
    """Using multiple independent if statements."""
    result = num
    if num < 100:
        result += 10
    if num < 200:
        result += 20
    if num < 300:
        result += 22
    if num >= 300:
        result += 25
    return result


def main():
    print("Program starting.")
    print("Testing decision structures.")
    
    num = int(input("Insert an integer: "))
    
    print("Options:")
    print("1 - In one multi-branched decision")
    print("2 - In multiple independent if-statements")
    print("0 - Exit")
    
    choice = int(input("Your choice: "))
    
    if choice == 1:
        print("Using one multi-branched decision structure.")
        result = multi_branched_decision(num)
        print(f"Result is {result}")
    elif choice == 2:
        print("Using multiple independent if statements.")
        result = multiple_independent_ifs(num)
        print(f"Result is {result}")
    elif choice == 0:
        print("Exiting program.")
    else:
        print("Invalid choice.")
    
    print("\nProgram ending.")


if __name__ == "__main__":
    main()