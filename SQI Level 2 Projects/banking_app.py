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

def generate_account_number():
    """Generate a random 10-digit account number"""
    return random.randint(1000000000, 9999999999)

def sign_up():
    """Register a new user with system-generated account number"""
    print("""
          
            *************** SIGN UP PAGE ***************
          
          *************** Please Fill the Below to Register ***************

            """)

#  Name
    while True:
        full_name = input("Enter your full name: ").strip()
                                            ## VALIDATIONS 
        if not full_name:
            print("Full name cannot be left blank. Please enter a valid name")
            continue

        elif (len(full_name) < 4) or (len(full_name) > 255):
            print("The lenght of full name must be more than 4 and less than 255 character. Please enter a valid name")
            continue
        
        elif any(char.isdigit() for char in full_name):
            print("No digit is expected in your name. Please enter a valid name")
            continue
        break

# Username
    while True:
        username = input("Enter a username: ").strip()
        cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,) )
        count = cursor.fetchone()[0]

        characters = []
        for char in username:
            if char in (string.ascii_letters + "_") or char in string.digits :
                characters.append(True)
            else:
                characters.append(False)

        if not username:
            print("Username cannot be left blank")
            continue
        elif count > 0:
            print("Username already exists. Please choose another one. ")
            continue
        elif len(username) < 3 and len(username) > 20:
            print("Username is out of range. Please enter between 3 and 20 characters")
            continue
        elif all(characters) == False:
            print("Please enter a valid username that is Alpha Numeric with/without underscore only.")
            continue
        break


# Password
    while True:
        password = getpass("Enter your password: ").strip()

        if not password:
            print("Password cannot be left blank")
            continue
        elif len(password) < 8:
            print("Your password must be more than 8 characters")
            continue
        elif any(char for char in password if char.islower()) == False:
            print("Password must contain at least one lowercase")
            continue
        elif any(char for char in password if char.isupper()) == False:
            print("Password must contain at least one uppercase")
            continue
        elif any(char for char in password if char.isdigit()) == False:
            print("Password must contain at least one digit")
            continue
        elif any(True for char in password if char in string.punctuation) == False:
            print("Password must contain at least one special character")
            continue

        
        confirm_password = getpass("Confirm your password: ").strip()
        if password != confirm_password:
            print("Passwords do not match")
            continue
        break

# Initial Deposit
    while True:
        try:
            initial_deposit = float(input("Enter Initial deposit amount (#)>>> "))
            if initial_deposit < 0:
                print("Deposit amount must be non-negative")
                continue
            elif initial_deposit < 2000:
                print("Minimum amount to open an account is #2000.00")
                continue
        except ValueError:
            print("Deposit must be a number")
            continue
        # try:
        #     initial_deposit = float(input("Enter initial deposit amount: "))
        #     if initial_deposit < 0:
        #         print("Deposit amount must be non-negative")
        #         continue
        # except ValueError:
        #     print("Deposit must be a number")
        #     continue

        break



# Generate unique account number
    while True:
        account_number = generate_account_number()

        cursor.execute("SELECT COUNT(*) FROM users WHERE account_number = ?", (account_number,) )
        count = cursor.fetchone()[0]
        
        if count != 0:
            continue
        break


    
    # Hash password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    try:
        cursor.execute("""
        INSERT INTO users (account_number, full_name, username, password, balance) VALUES
        (?, ?, ?, ?, ?)
        """, (account_number, full_name, username, hashed_password, initial_deposit))
        conn.commit()

        print("\nAccount created successfully!")
        print(f"Your Account Number: {account_number}\n")
        log_in()
    except sqlite3.IntegrityError:
        print("Username already exists. Try a different one.")




###                         LOG IN 
def log_in():
    """          Log in an existing user      """
    print("""
                    *************** Log In Page ***************

                    Please fill the below to log in to your account.

          """)

    while True:
        username = input("Enter your username: ").strip()
        if not username:
            print("Username cannot be left blank")
            continue
        break

    while True:
        password = getpass("Enter your password: ")
        if not password:
            print("Password cannot be left blank")
            continue
        break

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("SELECT account_number, full_name FROM users WHERE username = ? AND password = ?", 
                   (username, hashed_password))
    user = cursor.fetchone()

    if user:
        print(f"Login successful! Welcome, {user[1]}.")
        user_dashboard(user[0])
    else:
        print("Invalid credentials. Please try again.")




###                         DEPOSIT

def deposit(account_number):
   
    """     Deposit money into the user's account    """
    print("*************** Deposit ***************")

    while True:
        try:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                print("Deposit must be a positive number.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid amount to deposit.")
            continue
        break

    cursor.execute("UPDATE users SET balance = balance + ? WHERE account_number = ?", (amount, account_number))
    cursor.execute("INSERT INTO transactions (account_number, type, amount) VALUES (?, 'Deposit', ?)", 
                   (account_number, amount))
    conn.commit()
    print(f"Deposit of #{amount} is successful!")


###                         WITHDRAW
def withdraw(account_number):
    """     Withdraw money from the user's account      """
    print("*************** Withdraw ***************")

    while True:
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid amount to withdraw.")
            continue
        break

    cursor.execute("SELECT balance FROM users WHERE account_number = ?", (account_number,))
    balance = cursor.fetchone()[0]

    if balance >= amount:
        cursor.execute("UPDATE users SET balance = balance - ? WHERE account_number = ?", (amount, account_number))
        cursor.execute("INSERT INTO transactions (account_number, type, amount) VALUES (?, 'Withdrawal', ?)", 
                       (account_number, amount))
        conn.commit()
        print(f"Withdrawal of #{amount} is successful!")
    else:
        print("Insufficient funds!")

###                         CHECK BALANCE
def check_balance(account_number):
    """Display the user's current balance"""
    print("*************** Balance Inquiry ***************")

    cursor.execute("SELECT balance FROM users WHERE account_number = ?", (account_number,))
    balance = cursor.fetchone()[0]
    print(f"Your current balance is: #{balance}")



###                         TRANSACTION HISTORY
def transaction_history(account_number):
    """Display the user's transaction history"""
    print("*************** Transaction History ***************")

    cursor.execute("SELECT type, amount, timestamp FROM transactions WHERE account_number = ?", (account_number,))
    transactions = cursor.fetchall()

    if transactions:
        for trans in transactions:
            print(f"{trans[2]} - {trans[0]}: {trans[1]}")
    else:
        print("No transactions found.")


###                         ACCOUNT DETAILS
def account_details(account_number):
    """Display user's account details"""
    print("*************** Account Details ***************")

    cursor.execute("SELECT full_name, username, account_number FROM users WHERE account_number = ?", 
                   (account_number,))
    user = cursor.fetchone()
    print(f"Full Name: {user[0]}")
    print(f"Username: {user[1]}")
    print(f"Account Number: {user[2]}")



###                         DASHBOARD
def user_dashboard(account_number):
    """User dashboard after login"""
    while True:
        print("""
                            *************** Banking System ***************
                1. Deposit
                2. Withdraw
                3. Check Balance
                4. Transaction History
                5. Account Details
                6. Logout
        """)

        choice = input("Select an option: ")

        if choice == "1":
            deposit(account_number)
        elif choice == "2":
            withdraw(account_number)
        elif choice == "3":
            check_balance(account_number)
        elif choice == "4":
            transaction_history(account_number)
        elif choice == "5":
            account_details(account_number)
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")



###                         MAIN
def main():
    """Main function to run the banking system"""
    while True:
        print("""
                *************** Richie Mighty Commercial Banking System ***************

                Hello, welcome to Richie Mighty Commercial Bank. We are here to serve you. 
              Please select Sign Up or Log in to perform transactions. Thank You.

                        1. Sign Up
                        2. Log In
                        3. Exit
        """)

        choice = input("Select an option: ")

        if choice == "1":
            sign_up()
        elif choice == "2":
            log_in()
        elif choice == "3":
            print("Goodbye! Thank You for Banking with Richie.")
            break
        else:
            print("Invalid choice. Please try again.")

# if __name__ == "__main__":
main()
