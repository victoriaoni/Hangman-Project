import random
#tf
# Write code that will continuously ask the user for a letter and validate it.

word_list=['Mango', 'Apple', 'Banana', 'Pineapple', 'Strawberry']
word=random.choice(word_list)
#print(word)

while True:
    guess = input("Guess a letter: ").lower()    
    
    def ask_for_input():
        if len(guess) == 1 and guess.isalpha():
            
            def check_guess(guess):
                if guess in word:
                    print(f"Good guess! {guess} is in the word.")                 
                else:
                    print("Invalid letter. Please, enter a single alphabetical character.")  
            check_guess(guess)
    break
ask_for_input()




    
            
    
