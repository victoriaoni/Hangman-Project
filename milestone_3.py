import random

word_list=['Mango', 'Apple', 'Banana', 'Pineapple', 'Strawberry']
word=random.choice(word_list)
#print(word)


while True:
    guess = input("Guess a letter: ").lower()
    break    
#print(guess)
            
def check_guess(guess):
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

def ask_for_input():
    if len(guess) == 1 and guess.isalpha():
        #print('valid input')

        check_guess(guess)
            
ask_for_input()

