# names = "Ella", "MJ", "Augusta", "MJ"
# first_person, second_person, thrid_person, fourth_person = names

# print("first_person", first_person)
# print("second_person", second_person)
# print("thrid_person", thrid_person)
# print("fourth_person", fourth_person)




# colors = ("green", "yellow", "red")
# col1, col2, col3 = colors
# print(col1)
# print(col2)
# print(col3)



import random 
number = random.randint(1, 10)



i = 1
while i <= 5:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("You guessed correctly")
        break
    elif guess < number:
        print("Guess higher")
    else:
        print("Guess lower, Try again")
    i += 1



# Write a program that takes an integer n from the user and calculates the sum of all
# natural numbers up to n using a while loop.
n = int(input("Enter a number: "))
sum = 0
while n > 0:
    sum += n
    n -= 1








