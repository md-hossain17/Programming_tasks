# Interactive version that asks multiple times
while True:
    Name = input("What is your name (type 'quit' to exit): ")
    
    if Name.lower() == 'quit':
        print("Goodbye!")
        break
    
    print(f"Hi there {Name}")
    print()  # Empty line for readability