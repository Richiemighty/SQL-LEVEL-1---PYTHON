# word1, word2 = input("Enter a two word string: ").split(" ")

# if word1.strip().lower()[0] == word2.strip().lower()[0]:
#     print("The words begin with the same letter")
# else:
#     print("The word does not begins with the same letter")

num = int(input("Enter a number: "))
sqrt = num ** (1/2)

if sqrt * sqrt == num:
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")