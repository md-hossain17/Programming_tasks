#Make Python program which does the following steps:

#Prompt user to insert
#A word
#A character
#Find if the character exists in the word. Possible prints below.
#Word "{WordFirst}" contains character "{Character}"
#Word "{WordFirst}" doesn't contain character "{Character}"
#Prompt user to insert one more word
#Compare the first word to the second word. Examples below:
#The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
#The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
#Both inserted words are the same alphabetically, "{WordFirst}"
#Example program run

#run 1 run 2 run 3
#Program starting.
print("Program starting.")
#Insert first word: apple apple apple
#String comparisons
print("string comparisons")
#Insert first word: beans
word1 = input("Insert first word: ")
#Insert a character: n
character = input("Insert a character: ")
##Word "beans" contains character "n"
if(character in word1):
    print(f'word "{word1}" contains character "{character}"')
else :
    print(f'word "{word1}" doesn\'t contain character "{character}"')
#Insert second word: banana
word2 = input("insert second word: ")
#The second word "banana" is before the first word "beans" alphabetically.
if(word1 > word2):
    print(f'The first word "{word1}" is before the second word "{word2}" alphabetically.')
elif(word1 > word2):
    print(f'The second word "{word2}" is before the first word "{word1}" alphabetically.')

#Program ending.
print("Program ending.")