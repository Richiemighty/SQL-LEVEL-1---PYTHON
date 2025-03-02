# # 2. Write a program that simulates a grocery store checkout. 
# # The user should enter the prices of items until they decide to stop. 
# # # The program should calculate and display the total cost.

# while  True:
#     item_price = float(input("Enter prices of items: "))
#     # print(f"Enter item Price: {item_price}")

#     ask = input("Enter another item? (yes/no): ").strip().lower()
#     if ask != "yes":
#         break
    

# # 3. Write a program that continuously prompts the user to enter a password until they enter a valid one. 
# # A valid password must be at least 8 characters long and have a maximum of 25 characters.
# # Sample Input and Output:

# from getpass import getpass

# while True:
#     password = getpass("Enter password: ")

#     if len(password) >= 8 and len(password) <= 25:
#         print("Password accepted.")
#         break
#     else:
#         print("Password must be at least 8 characters long and have a maximum of 25 characters.")


# # 4.  4.	Write a program that asks for the user's age and keeps prompting them until they 
# # 	enter a valid age (greater than or equal to 0).
# # 	Sample Input and Output:

# while True:
#     age = int(input("Enter your age: "))

#     if age >= 0:
#         print("Age accepted")
#         break
#     else:
#         print("Invalid age. Please enter a valid age.")


# 5.  5. 	Write a program that tracks the inventory of items in a store. The user should be able 
	# to add or remove items and the program should display the current inventory after each
	# operation. The program stops when the user decides to exit.
	# The current store inventory is {‘eggs’: 40, ‘fish’: 200, ‘bread’: 343, ‘yam’:2}
	# Sample Input and Output:
	# Enter operation (add/remove/exit): add

# current_inventory = {"eggs": 40, "fish": 200, "bread": 343, "yam":2}

# while True :
#     prompt = input("Enter operation (add/remove/exit): ").strip().lower()
    
#     if prompt not in ['add', 'remove', 'exit']:
#         print("Please enter any of the three option (add/remove/exit) ")

#     elif prompt != "exit":
#         item = input("Enter item: ").strip().lower()
#         quantity = int(input("Enter quantity: "))

#         if prompt == "add":
#             current_inventory[item] += quantity 
#             print(f"Current Inventory:  {current_inventory}")
#         elif prompt == "remove":
#             current_inventory[item] -= quantity 
#             print(f"Current Inventory:  {current_inventory}")
#     else:
#         break
        



# phrase = input("Enter a Phrase: ").strip(" ").split(" ")
# acronym = ""

# for word in phrase:
#     acronym += word[0].upper()

# print(acronym)


# phrase = input("Enter a Phrase: ").strip(" ").split(" ")
# acronym = ""
# index = 0

# while index < len(phrase):
#     acronym += phrase[index][0].upper()
#     # print(phrase[index])
#     index += 1

# print(acronym)



st = "Print every word in this sentence that has an even number of letters"
word = st.split(" ")

i = 0
while i < len(word):
    if (len(word[i]) % 2) == 0:
        print(word[i])
    i+=1







