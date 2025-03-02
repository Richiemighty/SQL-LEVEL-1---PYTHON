# # Countdown from user input to zero
# number = int(input("Enter a number to start the countdown: "))
# while number >= 0:
#     print(number)
#     number -= 1




# # Print all even numbers from 1 to n
# n = int(input("Enter a number to print all even numbers up to: "))
# i = 2
# while i <= n:
#     print(i)
#     i += 2




# # Calculate base raised to the power of exponent using a while loop
# base = int(input("Enter the base: "))
# exponent = int(input("Enter the exponent: "))

# result = 1
# count = 0
# while count < exponent:
#     result *= base
#     count += 1

# print(f"{base} raised to the power of {exponent} is {result}")






# # Count the number of vowels in a string
# string = input("Enter a string: ").lower()
# vowels = "aeiou"
# count = 0
# index = 0

# while index < len(string):
#     if string[index] in vowels:
#         count += 1
#     index += 1

# print(f"The number of vowels in the string is: {count}")




# i = 1
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     print(i)


i = 1
while i < 11:
    print(i)
    i += 1


# Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop.

n = int(input("Enter a number: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1


# print(f"The sum of all natural numbers up to {n} is {sum}")


# Write a program that takes an integer n from the user and calculates the product of all
product = 1
i = 1
while i <= n:
    product *= i
    i += 1

print(product)



#

import random

number = random.randint(1, 51)
attempt = 5
i = 1
guess = int(input("Enter a guess"))
while i <= attempt:
    if guess == number:
        print("You guessed correctly")
        break
    elif guess < number:
        print("Guess higher")
    else:
        print("Guess lower")
    i -= 1


# Write a program that takes an integer n from the user and calculates the sum of all even numbers up to n using a while loop.