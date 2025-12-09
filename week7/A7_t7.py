# main.py

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ROTOR_I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

def main():
    print("Enigma Machine")
    
    # Initialize
    rotors = [ROTOR_I, ROTOR_II, ROTOR_III]  # Left to right
    reflector = REFLECTOR_B
    positions = [0, 0, 0]
    
    while True:
        # Reset for new message
        positions = [0, 0, 0]
        
        text = input("\nEnter text: ").upper().strip()
        if not text:
            print("Shutdown.")
            break
        
        result = []
        for char in text:
            if char not in ALPHABET:
                result.append(char)
                continue
            
            # Rotate
            positions[2] = (positions[2] + 1) % 26
            if positions[2] == 0:
                positions[1] = (positions[1] + 1) % 26
                if positions[1] == 0:
                    positions[0] = (positions[0] + 1) % 26
            
            # Forward pass
            c = char
            for i in [2, 1, 0]:  # Right to left
                idx = ALPHABET.index(c)
                shifted = (idx + positions[i]) % 26
                out = rotors[i][shifted]
                new_idx = (ALPHABET.index(out) - positions[i]) % 26
                c = ALPHABET[new_idx]
            
            # Reflector
            idx = ALPHABET.index(c)
            c = reflector[idx]
            
            # Reverse pass
            for i in [0, 1, 2]:  # Left to right
                idx = ALPHABET.index(c)
                shifted = (idx + positions[i]) % 26
                in_char = ALPHABET[shifted]
                
                # Find reverse mapping
                for j in range(26):
                    if rotors[i][j] == in_char:
                        new_idx = (j - positions[i]) % 26
                        c = ALPHABET[new_idx]
                        break
            
            result.append(c)
        
        print(f"Encrypted: {''.join(result)}")

if __name__ == "__main__":
    main()