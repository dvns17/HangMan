'''
Created on Nov 23, 2019

@author: ITAUser
'''
#import the random library

#def a function called pick_random_word():
    #open and read word dictionary/list(words.txt)
    
    #variable called index = selects random word from word.txt
    #variable called word = strip the randomly selected word
    #return the variable 'word'
    
#define a function called ask_for_next_letter():
    #variable called letter + input function that asks yuser to select a letter
    #return_letter_selected
    
# Define a function
#called generate_word_string(word,letters_guessed):
    #variable called output = empty lists
    #make a for loop that goes through each letter in the variable 'word':
        #and if statement that checks if letter is in letters_guessed:
            #append letter to output 
        #else:
            #append("_")
        #return output as a strint 
        
#create a main module:
    #variable called WORD = pick random words
    
    #variable called letters_to_guess = set of WORD
    #variable called correct_letters_guessed _ empty set
    #variable incorrect_letters_guessed = empty set
    #variable called number_of_guesses = number of guesses  
    
#print statement that welcomes the user to handman 

#while loop that runs until number_of_guesses < 1 or letters_to_guess is greater than zero:
    #variable called guess = ask_for_next_letter() and turn into lower case

    #if statement that checks if guess is in correct_letters_guessed or guess is in incorrect_letters_guesses:
        #print statement that says you have already guessed that letter
        
    #if statement checks if guess is in letters_to_guessed
        #remove guess from letters_to_guess
        #add guess to correct_letters_guessed
        #add guess to incorrect_letters_guessed
        #number_of_guesses goes down by one
        
    #variable called word_string = generate _word_string(Word, correct_letters_guessed)
    #print statement that prints word_string
    #print statement that print how many guesses you have left
    
    #if statement to check if numbers of guesses is less than one;
        #print congratulations you guessed the word right
    #else: 
        #print sorry you lost
    