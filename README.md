# Project Documentation Guideline for Hangman 

## Purpose of this document:
This document describes the code written for Milestone 2 of the Hangman game. This milestone creates variables for the game.

## Introduction:
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain number of attempts.  
This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Technologies:
The game is written using Python 3 and VSCode as the integrated development environment (IDE).  
Git is used for version control so I installed Git Bash, as I am using Windows.  

Github is used to host the code online so a new remote repository (repo) was created on GitHub and cloned locally. The cloned repo is the local version where the code will be saved initially, and when the code is ready, git commands are used to send the code from the local repo to the remote Github repo via the terminal in VSCode.

These are some commands I used for moving code from my local directory to the GitHub repository:  

`git status`  
This shows the files that have changed locally since the last snapshot saved on the remote Github repo.  
`git add .`  
This shows the changes that will be added, also known as staging.  
`git commit -m`  
This is where the comments are used to describe what the code will do are written.  
`git push`  
This command sends the changes from the local repo to the remote Github repo.  
  

I used the git command ‘touch’ to create a file named milestone_2.py from the VSCode terminal:
touch milestone_2.py 
This python file contains the code for this milestone. 
  
There are 5 tasks within this milestone.  

## Task 1 – Define the list of possible words:
In Python, lists are used to store multiple data in a single variable. 
I created a list containing the names of my 5 favourite fruits and assigned it to a variable called word_list:  
`word_list=['Mango', 'Apple', 'Banana', 'Pineapple', 'Strawberry']`    
This command prints the list to the screen:  
`print(word_list)`.
  
## Task 2 – Choose a random word from the list
Here I used the random module (one of Python's built-in modules), and it’s `choice` method which returns a random item from the list.  

The `import` keyword is written on the first line of the file to import the random module:
`import random
word_list=['Mango', 'Apple', 'Banana', 'Pineapple', 'Strawberry']`.  

The `random.choice` method is created, the word_list variable is passed into it and the randomly generated word is assigned to a variable called word:  
`word=random.choice(word_list)`  

Finally, the code is printed to screen:
print(word).
The code is run by typing `python milestone_2.py`.  
Each time the code is run a different fruit is printed to the screen. 

## Task 3 – Ask user for an input
The `input()` function in Python allows user input to be taken from the screen.
The input function asks the user to enter a single letter, and the input is assigned to a variable called guess.  
`guess = input("Enter a single letter: ")`.

## Task 4 – Check that user input is a single character
When taking input from users, it is best to validate that the input makes sense. This task checks to see whether only a single character is entered and that it is an alphabet. 
This is done by creating conditional checks that must be passed before the input can be accepted.

An `if` statement checks whether the length of the input is equal to 1 and that the input is an alphabet.
If the 2 conditions are met a message is printed to screen saying "Good guess!".  
`if len(guess) == 1 and guess.isalpha()  
      print ('Good guess!')`  
If either of the 2 preceding conditions are not met, an else block is created that prints "Oops! That is not a valid input."  
`else:
       print ('Oops! That is not a valid input.')`
     
## Task 5 - Start documenting the code written 
This is the creation of this markdown document (README.md), to describe the code written in Milestone 2 of the Hangman game.  

This document will be uploaded to Github via the VSCode terminal.
