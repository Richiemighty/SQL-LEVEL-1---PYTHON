# Assignment: 6, 7 and 17 - 34


# 6. Create two string variables: first_name with value "John" and last_name with value "Doe". Concatenate them together and print the result.
first_name = "John"
last_name = "Doe"
print(first_name + last_name)


# 7. Create a string variable message with the value "Hello, ". Interpolate the variable name (assigned the value "Alice") into the message and print the result.
name = "Alice"
message = f"Hello, {name}"
print(message)



# 17.	Convert a string “James John Kennedy” called “names” to a list using the string .split() method. Store the result in a list called “names_list”
names = "“James John Kennedy"
names_list = names.split(" ")
print(names_list)


# 18.	You have a list of cities called cities_list containing ['New York', 'Los Angeles', 'Chicago']. Convert this list into a single string where each city is separated by a semicolon and a space. Store the result in a string called cities_string.
cities_list = ['New York', 'Los Angeles', 'Chicago']
cities_string = "; ".join(cities_list)
print(cities_string)


# 19.	Create a string variable sentence with the value "the quick brown fox jumps over the 
# lazy dog". Capitalize the first letter of the string and 
# print the result.
sentence = "the quick brown fox jumps over the lazy dog"
capitalized_sentence = sentence.capitalize()
print(capitalized_sentence)



# 20. 	Create a string variable book_title with the value "to kill a mockingbird". Capitalize 
# the first letter of each word and print the result.

book_title = "to kill a mockingbird"
first_capitalized = book_title.title()
print(first_capitalized)



# 21. 	Create a string variable text with the value "hello world". Count the number of 
# occurrences of the letter 'o' and print the result.
text = "hello world"
count_o = text.count('o')
print(count_o)




# 22. 	Create a string variable filename with the value "document.txt". Check if the string 
# starts with "doc" and print the result.

filename = "document.txt"
print(filename.startswith("doc"))



# 23.	Create a string variable url with the value "https://www.example.com". Check if the 
# string ends with ".com" and print the result.

url = "https://www.example.com"
print(url.endswith(".com"))



# 24.	Create a string variable phrase with the value "find the needle in the haystack". Find 
# the position of the word "needle" and print the result.

phrase = "find the needle in the haystack"
print(phrase.find("needle"))



# 25.	Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the 
# format() method to replace the placeholders with "Alice" and "Wonderland" and print the 
# Result. Bonus point if you can do it with the f-string and concatenation methods also.
template = "Hello, {}. Welcome to {}."
result_format = template.format("Alice", "Wonderland")
print(result_format)


name = "Alice"
place = "Wonderland"
result_f_string = f"Hello, {name}. Welcome to {place}."
print(result_f_string)


result_concatenation = "Hello, " + "Alice" + ". Welcome to " + "Wonderland" + "."
print(result_concatenation)



# 26.	Create a string variable `quote` with the value "To be or not to be". Find the position 
# of the word "not" and print the result.
quote = "To be or not to be"
print(quote.find("not"))



# 27.	Create a string variable word with the value "hello". Check if all characters in the 
# string are lowercase and print the result.
word = "hello"
result = word.islower()
print(result)





# 28.	Create a string variable shout with the value "HELLO". Check if all characters in the 
# string are uppercase and print the result.
shout = "HELLO"
result1 = shout.isupper()
print(result1)


# 29.	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# lowercase and print the result.
mixed_case = "PyThOn"
print(mixed_case.lower())

# 30. 	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# uppercase and print the result.
mixed_case = "PyThOn"
print(mixed_case.upper())


# 31. 	Create a string variable padded_text with the value " hello ".Remove leading whitespace and 
# print the result.
padded_text = " hello "
print(padded_text.lstrip())

# 32. 	Create a string variable padded_text with the value " hello ". Remove trailing whitespace and 
# print the result.
padded_text = " hello "
print(padded_text.rstrip())


# 33.	Create a string variable padded_text with the value " hello ". Remove both leading and trailing 
# whitespace and print the result.
padded_text = " hello "
print(padded_text.strip())


# 34.	Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" 
# and print the result.
greeting = "Hello, World!"
new_word = greeting.replace("World", "Alice")
print(new_word)