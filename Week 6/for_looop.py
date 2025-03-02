# my_row = ("Isreal", "HaYBee", "Richie", "FK", "Ola")

# for name in my_row:
#     print(name)


numbers = list(range(1,51))

multiples_of_5 = []

for multiple in numbers:
    if multiple % 5 == 0:
        multiples_of_5.append(multiple)
        
print(multiples_of_5)





end = int(input("Enter a Number: "))

for number in range(1, end+1):
    print(number)