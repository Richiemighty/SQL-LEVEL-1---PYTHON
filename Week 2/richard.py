# # 1. 
# name = input("What is your name? ")
# print(f"Hello, {name}!")


# # 2. 

# from datetime import datetime
# year = int(input("What is your years of birth? "))
# age = datetime.today().year - year
# print(f"You are {age} years old.")




# # 3.
# favourite_color= input("What is your Favourite Color? ")
# print(f"Your favorite color is {favourite_color}.")
      






# # 4.

# palindrome = input("Enter a word: ")
# if palindrome == palindrome[::-1]:
#     # print("It is a palindrome")
#     is_palindrome = True

# else:
#     # print("It is not a palindrome")
#     is_palindrome = False

# print(f"It is {is_palindrome} that {palindrome} is a palindrome.”")


# # 5.
# from getpass import getpass

# password = getpass("What is your password? ")
# is_valid = True
# if len(password) == 8:
#     is_valid = True
# else:
#     is_valid = False

# print(f"It is {is_valid} that the password fulfils the criteria.")





# # 6.

# weight = float(input("Enter your weight (in kilograms): "))
# height = float(input("Enter your height (in meters): "))

# BMI = weight / (height ** 2)


# print(f"Your BMI is {BMI:.2f}")







richard = [1,2,3,4,5,5,7,3,4]

print(sum(richard)/len(richard))