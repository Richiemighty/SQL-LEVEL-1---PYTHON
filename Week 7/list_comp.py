# states = ['Osun', 'Anambra', 'Oyo', 'Kano']
# states_that_starts_with_o = [state for state in states if state.startswith('O')]
# print(states_that_starts_with_o)



# nums = [3, 8, 4, 18, 20, 21, 25, 30]
# are_divisible_by_3 = []

# for num in nums:
#     if num % 3 == 0:
#         are_divisible_by_3.append(True)
#     else:
#         are_divisible_by_3.append(False)
# print(are_divisible_by_3)


# are_divisible_by_3 = [num % 3 == 0 for num in nums]
# print(are_divisible_by_3)




# # divisible_by_3 = [num for num in nums if (num % 3) == 0 ]
# # print(divisible_by_3)



# greater_20 = [num for num in nums if num > 20 ]
# print(greater_20)



# mul_of_5 = [num for num in range(5, 501) if num % 5 == 0]
# print(mul_of_5)


# animals = ['zebra', 'giraffe', 'tiger', 'goat', 'dog', 'turtle']

# animals_uppercase = [animal.upper() for animal in animals]
# print(animals_uppercase)


# len_animals = [len(animal) for animal in animals]
# print(len_animals)


# letter_a = all("a" in animal for animal in animals)

# letter_a = all("a" in animal for animal in animals)
# print(letter_a)




# names = ["andrew", "jesu", "oliver", "richie", "emma", 'ursula', "winnie", "ivan", "ethan","olga", "uma", "alex", "erin"]
# vowels = ('a', 'e', 'i', 'o', 'u')

# final_names = [name[::-1].upper() for name in names if name.startswith(vowels) and len(name) > 3]
# print(final_names)



name = "james"  
event = "Tech Conference"  
date = "25th February 2025"  

# Write a program to format the invitation using string interpolation and capitalize the recipient's name.
# Print:

# print("Dear " + name.title() + ", you are cordially invited to the " + event + ". It will be held on " +  date)
# print("Dear " + name.title() + ", you are cordially invited to the " + event + ". It will be held on " +  date)




first_name = 'Richie'
Last_name = 'Mighty5'

email = first_name.lower() + Last_name.lower() + "@gmail.com"

print('@' in email)
print(email.startswith(first_name.lower()))
print(email.endswith(".com"))


print(f"""
It is {'@' in email} that your email contains @
It is {email.startswith(first_name.lower())} that it starts with your first name, Richie.
And it is also {email.endswith(".com")} it ends with .com
""")


product_name = 'Iphone 15'
launch_date = 'September 12, 2025'
standout_feature = "a revolutionary AI camera"



sentence = "Coding is fun when coding is understood"
print(sentence.lower().count('coding'))



sentence = "Learning Python is exciting!" 
character = "P"

print(sentence.find(character))

print(float(5))


print(range.__doc__)

print("Hello", end=" ")
print("World")  # Output: Hello World (on the same line)





# You can also assign values to float type using scientific notations, which is useful when working with very large numbers. Try this example:
fval2 = 4.6e7
print(fval2)


