# name = "richard"
# age = 43

# print(f"My name is {name} and im {age} years old")
# print("My name is {1} and im {0} years old".format(name, age))


# print(name.find("q"))
# print(name.index("a"))



# message = "@h the of th @ hfkr gjskn"
# print(message.replace("the", "with"))


# text = message.split()
# print(text)



# names = ("Richard", "King")
# print("&".join(names))




# text = " hello WORLD ".strip().capitalize() + "."
# print(text)


# Extract and preprocess the components:
# Author: Capitalize the first letter of the author's names i.e. title case
# Book Title: Trim any leading and trailing whitespaces and convert the title to be in title case.
# ISBN Number: Correct the typo in the ISBN number by replacing ISN with ISBN.
# Cost: Format the cost to 2 decimal places and prepend the naira symbol ₦.
# Format the information into a new multi-line string called `formatted_book_info` using an f-string or the format method.
# The output should be of the format:
# The book `book_title` was written by `author` and published in `year_published`.
# It has `no_of_pages` pages and `isbn` and costs `cost`.
# Using the example above, the expected output is: 
# The book The Art Of Programming was written by John Doe and published in 2020.
# It has 350 pages and ISBN 978-3-16-148410-0 and costs ₦2500.00.

# Steps:
# Split the `book_info` string into its components using `.split(“ ; “)`.
# Preprocess each component as described.
# Create and print the `formatted_book_info` string.



book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"
splitted = book_info.split(";")
author = splitted[0].title().strip()
book_title = splitted[1].strip().capitalize()
year_published = splitted[2].strip()
no_of_pages = splitted[4]
isbn = splitted[3].strip().replace("ISN", "ISBN")
cost = float(splitted[5])


output = f"""
The book {book_title} was written by {author} and published in {year_published}.
It has {no_of_pages} pages and {isbn} and costs {cost}.
"""
print(output)