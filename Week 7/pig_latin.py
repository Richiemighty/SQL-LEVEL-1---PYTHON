# word = input("Enter a word: ")
word = 'young'
vowels = "aeiouy"
pig_latin = ""


for i in word:
    if word[0] == 'y':
        pig_latin = word[1: ] + word[0] + 'ay'
    elif word[0] in vowels:
        pig_latin = word + 'way'
    elif i in vowels:
        pig_latin = word[word.index(i): ] + word[:word.index(i)] + 'ay'
        break
print(pig_latin)






