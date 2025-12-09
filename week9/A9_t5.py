def main():
    try:
        # Get inputs
        r_str = input()
        g_str = input()
        b_str = input()
        
        # Try to convert to integers - will fail for non-numeric, floats, etc.
        r = int(r_str)
        g = int(g_str)
        b = int(b_str)
        
        # Check if the string representation matches exactly (catches floats like "3.14")
        # Also handle negative signs
        def is_exact_integer(s, val):
            s = s.strip()
            if s.startswith('-'):
                return s == str(val)
            return s == str(val) and not '.' in s
        
        if not (is_exact_integer(r_str, r) and 
                is_exact_integer(g_str, g) and 
                is_exact_integer(b_str, b)):
            raise ValueError("Not exact integer")
        
        # Check range
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("Out of range")
        
        # Display results
        print(f"#{r:02x}{g:02x}{b:02x}")
        print(f"{r:08b}")
        print(f"{g:08b}")
        print(f"{b:08b}")
        
    except ValueError:
        print("Couldn't perform the designed task due to the invalid input values.")

if __name__ == "__main__":
    main()