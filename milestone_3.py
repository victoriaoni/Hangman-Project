import random

word_list=['Mango', 'Apple', 'Banana', 'Pineapple', 'Strawberry']
word=random.choice(word_list)
#print(word)
while True:
    guess = input("Guess a letter: ")
    if len(guess) == 1 and guess.isalpha():
        if guess in word:
            print("Good guess! " + guess + " is in the word.")
            
        else:
            print("Sorry, " + guess + " is not in the word. Try again.") 
    break   
    