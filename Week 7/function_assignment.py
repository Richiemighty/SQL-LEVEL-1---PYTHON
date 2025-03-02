# 1. Write a function sum_numbers(a, b) that returns the sum of two numbers.
def sum_numbers(a, b):
    return a + b


print("sum_numbers(3, 5):", sum_numbers(3, 5))  



# 2. Write a function is_even(n) that returns True if n is even and False if n is odd.
def is_even(n):
    return n % 2 == 0

print("is_even(4):", is_even(4))  
print("is_even(5):", is_even(5))  


# 3. Write a function is_prime(n) that returns True if n is a prime number and False otherwise.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("is_prime(7):", is_prime(7))  
print("is_prime(10):", is_prime(10))  

# 4. Using the is_prime(n) function from number 3, write a function that asks a user for an input
#  n and returns all the prime numbers up to n.
def primes_up_to_n():
    n = int(input("Enter a number: "))
    return [i for i in range(2, n + 1) if is_prime(i)]

print("Primes up to 10:", primes_up_to_n())  



# 5. Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both
#  numbers are even, but returns the greater if one or both numbers are odd.
def lesser_of_two_evens(a, b):
    if is_even(a) and is_even(b):
        return min(a, b)
    return max(a, b)

print("lesser_of_two_evens(2, 4):", lesser_of_two_evens(2, 4))  
print("lesser_of_two_evens(2, 5):", lesser_of_two_evens(2, 5))  



# 6. Write a function is_alliteration(two_word_string) that takes a two-word string and returns
#  True if both words begin with the same letter.
def is_alliteration(two_word_string):
    words = two_word_string.lower().split()
    return words[0][0] == words[1][0]

print("is_alliteration('Levelheaded llama'):", is_alliteration('Levelheaded llama'))  
print("is_alliteration('Crazy Kangaroo'):", is_alliteration('Crazy Kangaroo'))  



# 7. Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name.
def old_macdonald(name):
    if len(name) < 4:
        return name.capitalize()
    return name[:3].capitalize() + name[3:].capitalize()
print("old_macdonald('macdonald'):", old_macdonald('macdonald'))  



# 8. Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
def spy_game(list_of_ints):
    code = [0, 0, 7]
    for num in list_of_ints:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False


print("spy_game([1, 2, 4, 0, 0, 7, 5]):", spy_game([1, 2, 4, 0, 0, 7, 5]))  
print("spy_game([1, 0, 2, 4, 0, 5, 7]):", spy_game([1, 0, 2, 4, 0, 5, 7]))  
print("spy_game([1, 7, 2, 0, 4, 5, 0]):", spy_game([1, 7, 2, 0, 4, 5, 0]))  




# 9. Write a function vol(radius) that computes the volume of a sphere given its radius.
def vol(radius):
    return (4 / 3) * 3.141592653589793 * radius**3

print("vol(3):", vol(3))  




# 10. Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).
def range_check(num, low, high):
    return low <= num <= high
print("range_check(5, 1, 10):", range_check(5, 1, 10))  
print("range_check(0, 1, 10):", range_check(0, 1, 10))  



# 11. Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.
def upper_lower(text):
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    return {"uppercase": upper, "lowercase": lower}
print("upper_lower('Hello World!'):", upper_lower('Hello World!'))  


# 12. Write a function unique_list(list_items) that takes in a list and returns a new list with unique 
# elements of the first list. Do not use the set() constructor.
def unique_list(list_items):
    unique = []
    for item in list_items:
        if item not in unique:
            unique.append(item)
    return unique
print("unique_list([1, 2, 2, 3, 4, 4]):", unique_list([1, 2, 2, 3, 4, 4]))  



# 13. Write a function multiply(list_items) to multiply all the numbers in a list.
def multiply(list_items):
    result = 1
    for item in list_items:
        result *= item
    return result

print("multiply([1, 2, 3, -4]):", multiply([1, 2, 3, -4]))  



# 14. Write a function is_pangram(text) to check whether a string is a pangram or not.
def is_pangram(text):
    import string
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(text.lower())

print("is_pangram('The quick brown fox jumps over the lazy dog'):", is_pangram('The quick brown fox jumps over the lazy dog'))  
print("is_pangram('Hello World'):", is_pangram('Hello World'))  



# 15. Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each other.
def are_anagrams(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

print("are_anagrams('spar', 'rasp'):", are_anagrams('spar', 'rasp'))  
print("are_anagrams('hello', 'world'):", are_anagrams('hello', 'world'))  



# 16. Write a function calculate_bmi(weight, height) that calculates the Body Mass Index (BMI) given 
# weight in kilograms and height in meters.
def calculate_bmi(weight, height):
    return weight / (height**2)

print("calculate_bmi(70, 1.75):", calculate_bmi(70, 1.75))  


# 17. Write a function calculate_simple_interest(principal, rate, time) that calculates the simple 
# interest given principal amount, interest rate, and time (in years).
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print("calculate_simple_interest(1000, 5, 2):", calculate_simple_interest(1000, 5, 2))  
