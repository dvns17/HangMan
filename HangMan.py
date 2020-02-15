import string
from pip._vendor.requests.adapters import DEFAULT_RETRIES
Objective: The objective of this program is to make a hangman game.

Algorithm:
    1) Define a function that randomly selects a word from a text dictionary/list
    2) Define a function that takes imput from the user for each letter guessed
    3) Define a function that will take the letter guessed correctly and turn it into a string
    4) Create variables to store data that the user enters
        a) create a varible that stores the word that the computer picks
        b) create 2 variables, one that holds the correct letters guessed and one that holds the wrong letters guessed
    5) Display an introduction to the program so the users will know what to do
    6)Create a loop that will allow the user to keep guessing until they win, or run out of trys
    7) Add statement at the beginning and the end of the game to welcome users and thank them for playing
    