DELIMITER = ','

def collectWords():
    """Collects words from user until empty input, returns words as delimited string"""
    words = []
    
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        words.append(word)
    
    # Join all words with the delimiter
    return DELIMITER.join(words)

def analyseWords(words_string):
    """Analyses words and displays statistics, returns nothing"""
    # Split words using the delimiter
    words = words_string.split(DELIMITER)
    
    # Calculate statistics
    word_count = len(words)
    char_count = sum(len(word) for word in words)
    
    # Calculate average word length
    if word_count > 0:
        avg_length = char_count / word_count
    else:
        avg_length = 0.0
    
    # Display results
    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print(f"- {avg_length:.2f} Average word length")

def main():
    """Main program logic"""
    print("Program starting.")
    
    # Collect words
    collected_words = collectWords()
    
    # Analyze words
    analyseWords(collected_words)
    
    print("Program ending.")

if __name__ == "__main__":
    main()