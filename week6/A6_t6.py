# main.py

# Constants for alphabets
LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftCharacter(char: str, alphabet: str) -> str:
    """
    Shift a character by 13 positions within the given alphabet
    
    Args:
        char: Single character to shift
        alphabet: The alphabet to use (lowercase or uppercase)
        
    Returns:
        Shifted character or original if not in alphabet
    """
    if char in alphabet:
        # Find current position and shift by 13
        pos = alphabet.index(char)
        # ROT13: shift by 13 positions, wrap around using modulo
        new_pos = (pos + 13) % 26
        return alphabet[new_pos]
    return char

def rot13(text: str) -> str:
    """
    Apply ROT13 cipher to a string
    
    Args:
        text: Input text to encrypt
        
    Returns:
        ROT13 encrypted text
    """
    result = []
    
    for char in text:
        if char in LOWER_ALPHABETS:
            # Shift lowercase letters
            result.append(shiftCharacter(char, LOWER_ALPHABETS))
        elif char in UPPER_ALPHABETS:
            # Shift uppercase letters
            result.append(shiftCharacter(char, UPPER_ALPHABETS))
        else:
            # Keep non-alphabet characters unchanged
            result.append(char)
    
    return ''.join(result)

def writeFile(filename: str, content: str) -> None:
    """
    Write content to a file with UTF-8 encoding
    
    Args:
        filename: Name of the file to write
        content: Content to write to the file
    """
    try:
        with open(filename, 'w', encoding="UTF-8") as file:
            file.write(content)
        print(f"File '{filename}' saved successfully.")
    except Exception as e:
        print(f"Error saving file: {e}")

def main() -> None:
    """
    Main program: Collects text, applies ROT13, saves to file
    """
    print("ROT13 Cipher Program")
    print("=" * 50)
    print("Enter text lines (empty line to finish):")
    
    # Collect multiple lines of text
    lines = []
    while True:
        try:
            line = input()
            if line == "":
                break
            lines.append(line)
        except EOFError:
            break
    
    if not lines:
        print("No text entered. Exiting.")
        return
    
    # Apply ROT13 to each line
    print("\nApplying ROT13 cipher...")
    ciphered_lines = []
    for line in lines:
        ciphered_line = rot13(line)
        ciphered_lines.append(ciphered_line)
    
    # Join lines with newlines
    ciphered_text = '\n'.join(ciphered_lines)
    
    # Display ciphered text
    print("\nCiphered text:")
    print("-" * 30)
    print(ciphered_text)
    print("-" * 30)
    
    # Ask for filename
    filename = input("\nEnter filename to save (or press Enter to skip): ").strip()
    
    if filename:
        writeFile(filename, ciphered_text)
    else:
        print("No filename provided. Text not saved.")

# Run the main function if executed directly
if __name__ == "__main__":
    main()