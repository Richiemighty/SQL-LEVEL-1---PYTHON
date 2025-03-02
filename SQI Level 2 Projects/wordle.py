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
# def display_board(attempts):
#     print("\n"+ tabulate(attempts, tablefmt="heavy_grid") + "\n")



# Function to play the game
def play_wordle():

    secret_word = random.choice(WORDS)  # Select a random word

    attempts = [ [" " for _ in range(5)] for _ in range(6) ]  # Empty board

    max_attempts = 6

    display_instructions()

    for attempt in range(max_attempts):

        while True:
            guess = input(f"Attempt {attempt + 1}/{max_attempts} - Enter a 5-letter word: ").lower().strip()
            if len(guess) == 5 and guess.isalpha():
                break
            print("Invalid input! Please enter a valid 5-letter word.")

        feedback = check_guess(guess, secret_word)

        attempts[attempt] = feedback  # Update board

        print("\n"+ tabulate(attempts, tablefmt="heavy_grid") + "\n")

        if guess == secret_word:
            print(colored("\n Congratulations! You guessed the word!", "green"))
            return

    print(colored(f"\n❌ You've used all attempts! The correct word was: {secret_word}", "red"))








# Run the game
if __name__ == "__main__":
    play_wordle()
