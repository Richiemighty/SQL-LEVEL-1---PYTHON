
# CONCATENATION


# My name is Richard and i live in Oyo. I am 100years old and it is True that i am a Female

name = "Richard"
location = "Oyo"
age = 100
is_female = False



sentence = "My name is " + name + " and i live in " + location + ". I am " + str(age) + " years old and it is " + str(is_female) + " that i am a Female"
print(sentence)


# INTERPORLATION

sentence1 = f"My name is {name} and i live in {location}. I am {age} years old and it is {is_female} that i am a Female"
print(sentence1)



sentence2 = "My name is {} and i live in {}. I am {} years old and it is {} that i am a Female".format(name, location, age, is_female)
print(sentence2)



# STRING METHODS
intro = "good morning"
print(intro.title())
print(intro.capitalize())
print(intro.upper())
print(intro.lower())




# COUNT
print(intro.count("o"))

