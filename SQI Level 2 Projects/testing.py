import sqlite3
import hashlib
import string
import random
from getpass import getpass


# Connect to SQLite database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create Users Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number INTEGER UNIQUE NOT NULL,
    full_name TEXT NOT NULL,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    balance REAL DEFAULT 0.0
)
""")

# Create Transactions Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number INTEGER NOT NULL,
    type TEXT NOT NULL,
    amount REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_number) REFERENCES users(account_number)
)
""")




# Example usage
username = "johnoe2*"

# result = all(True for char in username if char in string.ascii_letters or char in string.digits  )
# print(result)
# characters = []

# for i in username:
#     if i in (string.ascii_letters + "_") or i in string.digits :
#         characters.append(True)
#     else:
#         characters.append(False)

# print(characters)
# 

# for i in username:
#     if i in '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', '-', '.', '/', ':', ';', '<',
#               '=', '>', '?', '@', '[', '\', "]", '^', '`', '{', '|', '}', '~'


# print(string.)





# while True:
#     password = input("Enter your password: ")

#     have_lower = any(char for char in password if char.islower())   
#     have_upper = any(char for char in password if char.isupper())   
#     have_digit = any(char for char in password if char.isdigit())   
#     have_s_c = any(True for char in password if char in string.punctuation)
   
#     print(all([have_digit, have_lower, have_s_c, have_upper]))


#     # for char in password:
#     #     if char in string.ascii_lowercase:
#     #         print("Please add lowercase")
#     #         continue
#     #     elif char not in string.ascii_uppercase:
#     #         print("Please add uppercase")
#     #         continue
#     #     elif char not in string.digits:
#     #         print("Please add digits")
#     #         continue
#     #     elif char not in string.punctuation:
#     #         print("Please add special character")
#             # continue

#     break



# while True:
#     try:
#         initial_deposit = float(input("Enter Initial deposit amount (#)>>> "))
#         if initial_deposit < 0:
#             print("Deposit amount must be non-negative")
#             continue
#         elif initial_deposit < 2000:
#             print("Minimum amount to open an account is #2000.00")
#             continue
#     except ValueError:
#         print("Deposit must be a number")
#         continue

#     break
    
import random
from tabulate import tabulate
from termcolor import colored




# def check_guess(guess, secret_word):

#     feedback = []

#     for i in range(len(guess)):
#         if guess[i] == secret_word[i]:
#             feedback.append(colored(guess[i], 'red'))  # Correct position

#         elif guess[i] in secret_word:
#             feedback.append(guess[i])  # Correct position

#         else:
#             feedback.append(guess[i])  # Correct position
#     return feedback


# check_guess('richie', 'mighty')



import random
from tabulate import tabulate
from termcolor import colored


# List of 5-letter words
WORDS = ["apple", "grape", "mango", "peach", "lemon", "berry", "chili", "olive", "melon", "plumb"]

# # Colors for feedback
# GREEN = "\033[92m"   # Correct letter in the correct position
# YELLOW = "\033[93m"  # Correct letter in the wrong position
# RED = "\033[91m"     # Letter not in the word
# RESET = "\033[0m"    # Reset color


# Function to display game instructions
def display_instructions():
    print("""
                            ========================================
                            Welcome to Wordle - Text Version 
                            ========================================
                        Rules:
                        - Guess the 5-letter hidden word within 6 attempts.
                        - Letters in the **correct position** will be **GREEN**.
                        - Letters in the word but in the **wrong position** will be **YELLOW**.
                        - Letters **not in the word** will be **RED**.
                        - Good luck! 
    """)


# Function to generate feedback for the guessed word
def check_guess(guess, secret_word):

    feedback = []

    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            feedback.append(colored(guess[i], "green"))  # Correct position

        elif guess[i] in secret_word:
            feedback.append(colored(guess[i], "yellow"))  # Wrong position

        else:
            feedback.append(colored(guess[i], "red"))  # Not in word
    return feedback





# Function to display the Wordle board in a tabular format
def display_board(attempts):
    print("\n" + tabulate(attempts, tablefmt="grid") + "\n")



# Function to play the game
def play_wordle():

    secret_word = random.choice(WORDS)  # Select a random word

    attempts = [[" " for _ in range(5)] for _ in range(6)]  # Empty board

    max_attempts = 6

    display_instructions()

    for attempt in range(max_attempts):
        while True:
            guess = input(f"Attempt {attempt + 1}/{max_attempts} - Enter a 5-letter word: ").lower().strip()
            if len(guess) == 5 and guess.isalpha():
                break
            print("⚠️ Invalid input! Please enter a valid 5-letter word.")

        feedback = check_guess(guess, secret_word)
        
        attempts[attempt] = feedback  # Update board

        display_board(attempts)

        if guess == secret_word:
            print(colored("\n🎉 Congratulations! You guessed the word!", "green"))
            return

    print(colored(f"\n❌ You've used all attempts! The correct word was: {secret_word}", "red"))




# Run the game
if __name__ == "__main__":
    play_wordle()
