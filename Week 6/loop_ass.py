
# 10.	Write a program that takes an integer n from the user and calculates the sum of 
# squares of all numbers from 1 to n. Print the sum. Example:
# Input: 3
# Output: 14 (1^2 + 2^2 + 3^2)

n = int(input("Enter a number: "))

output = 0
calculations = ""
for i in range(1,n+1):
    output += i**2
    if i < n:
        calculations += f"{i}^2 + " 
    else:
        calculations += f"{i}^2" 


print(f"{output} => calculation: ({calculations})")



#  11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# 	letter of each word. Print the acronym. Example:
# 	Input: "Portable Network Graphics"
# 	Output: "PNG"

phrase = input("Enter a Phrase: ").strip(" ").split(" ")
acronym = ""
for word in phrase:
    acronym += word[0].upper()
print(f"Acronym of the phrase is {acronym}")

#  12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# 	Print the count. Example:
# 	Input: "Hello world from Python"
# 	Output: 4

string = input("Enter a String: ").strip().split(" ")

number = 0
for word in string:
    number += 1
print(f"Count of numbers = {number}")

#  13. 	Collect a string from the user and only print put the words that start with the letter 
# 	‘S’. Example:
# 	Input: “Print only the words that start with s in this sentence”
# 	Output: 
# 	start
# 	s
# 	Sentence

text = "Print only the words that start with s in this sentence"

words = text.strip().split(" ")
for word in words:
    if word[0].lower() == 's':
        print(word)


#  14. 	Print all the even numbers from 1 to 20 using the range function and a loop.

for i in range(1,21):
    if i % 2 == 0:
        print(i)


#  15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# 	by 3.
list_of_num = []
for i in range(1,51):
    if i % 3 == 0:
        list_of_num.append(i)

print(list_of_num)

#  10.	Go through the string below and if the length of a word is even, print that word.
# 	st = ‘Print every word in this sentence that has an even number of letters’
# 	Output: 
# 	word
# 	in
# 	this
# 	sentence
# 	that
# 	an
# 	even
# 	number
# 	of


st = "Print every word in this sentence that has an even number of letters"
word_list = st.split(" ")
for word in word_list:
    if len(word) % 2 == 0:
        print(word)




#  17. 	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# 	are multiples of both three and five, print “FizzBuzz”.

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        i = "FizzBuzz"
    elif i % 3 == 0:
        i = "Fizz"
    elif i % 5 == 0:
        i = "Buzz"
    else:
        i = i
    print(i)

