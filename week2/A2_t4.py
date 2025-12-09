
print("Program starting.\n")


word = input("Insert a closed compound word: ")


print(f"The word you inserted is '{word}' and in reverse it is '{word[::-1]}'.")
print(f"The inserted word length is {len(word)}")
print(f"Last character is '{word[-1]}'\n")


start = int(input("1) Starting point: "))
end = int(input("2) Ending point: "))
step = int(input("3) Step size: "))


substring = word[start:end:step]


print(f"\nThe word '{word}' sliced to the defined substring is '{substring}'.")
print("\nProgram ending.")