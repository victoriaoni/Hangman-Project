# Create a while loop and set the condition to True.

while True:
    guess = input("Guess a letter: ")
    if len(guess) == 1 and guess.isalpha():
        break    
    else:
        print("Invalid letter. Please, enter a single alphabetical character.") 
    break