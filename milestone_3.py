import random

word_list=['Mango', 'Apple', 'Banana', 'Pineapple', 'Strawberry']
word=random.choice(word_list)
print(word)

while True:
    guess = input("Guess a letter: ").lower()
    break
    print(guess)
    
#Define a function called ask_for_input.
#Move the code that you wrote in the Iteratively check if the input is a valid guess task into this function block.
def ask_for_input():
            if len(guess) == 1 and guess.isalpha():
                print("I guessed a single letter")  
     
# Define a function called check_guess. pass in the guess as a parameter for the function. 
            def check_guess(guess):
                if guess in word:
                    print("Good guess! " + guess + " is in the word.")
                
                else:
                    print("Sorry, " + guess + " is not in the word. Try again.") 

# Outside the while loop, but within the ask_for_input function, call the check_guess function to check if the guess is in the word.     
    
            check_guess(guess)  

ask_for_input() 


   
    
 