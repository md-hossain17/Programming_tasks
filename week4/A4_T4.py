print("Program starting.")

# Initialize counters
word_count = 0
char_count = 0

# Start prompting for words
while True:
    word = input("Insert word (empty stops): ")
    
    # Check if word is empty (user pressed enter without typing anything)
    if word == "":
        break
    
    # Update counters
    word_count += 1
    char_count += len(word)

print("\nYou inserted:")
print(f"- {word_count} words")
print(f"- {char_count} characters")

print("\nProgram ending.")