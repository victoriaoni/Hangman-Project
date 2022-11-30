
#Write code that will continuously ask the user for a letter and validate it.

while True:
    guess = input("Guess a letter: ")
    if len(guess) == 1 and guess.isalpha():
        break    
    else:
        print("Invalid letter. Please, enter a single alphabetical character.") 