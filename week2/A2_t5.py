print("Program starting.")
print()

# Get the compound word
word = input("Insert a closed compound word: ")

# Reverse the word
reversed_word = word[::-1]

# Get word length and last character
word_length = len(word)
last_char = word[-1]

print(f"The word you inserted is '{word}' and in reverse it is '{reversed_word}'.")
print(f"The inserted word length is {word_length}")
print(f"Last character is '{last_char}'")
print()

print("Take substring from the inserted word by inserting...")

# Get substring parameters
start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))
print()

# Create substring using slicing
substring = word[start:end:step]

print(f"The word '{word}' sliced to the defined substring is '{substring}'.")
print("Program ending.")