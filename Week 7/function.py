# from getpass import getpass

# password = "6richaRdddd@"

# length = len(password) >= 8
# is_upper = any(letter.isupper() for letter in password)
# is_lower = any(letter.islower() for letter in password)
# digit = any(num in "01234567" for num in password)
# character = any(char in "!@#$%^&*" for char in password)

# print(length and is_lower and is_upper and digit and character)

# def multiply(first_num, second_num):
#     return first_num * second_num

# print(multiply(3, 5))




# def upper_lower(text):
#     upper_count = 0
#     lower_count = 0
#     i = 0
#     while i < len(text):
#         if text[i].islower():
#             lower_count += 1
#         elif text[i].isupper():
#             upper_count += 1
#         i += 1
#     return lower_count, upper_count     


# print(upper_lower('Richard'))


numbers = range(0,21)

def mod(numbers):
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    print(even)

mod(numbers)


def even(start, end):
    list_evens = [i for i in range(start, end) if i % 2 == 0]
    print(list_evens)
mod(numbers)


evens = lambda start, end : [i for i in range(start, end) if i % 2 == 0]
# print(evens(0,21))


