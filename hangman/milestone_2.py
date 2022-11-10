import random
guess = input("Enter a single letter: ")
word_list=['Mango', 'Apple', 'Banana', 'Pineapple', 'Strawberry']
word=random.choice(word_list)
print(word)

if len(guess) == 1 and guess.isalpha():
      
      print ('Good guess!')
else:
       print ('Oops! That is not a valid input.')
     
