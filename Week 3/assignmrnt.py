# Task 1
fruits = ["apple", "banana", "orange"]
print(fruits[0]) 


# Task 2
colors = ["red", "green", "blue"]
print(colors[-1])  

# Task 3
numbers = list(range(1, 11))
print(numbers[3:8])  

# Task 4
alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
print(alphabets[-3:])  

# Task 5
ages = [20, 30, 40]
ages[1] = 35
print(ages)  

# Task 6
grades = ["A", "B", "C", "D"]
grades[1:3] = ["X"]
print(grades)  

# Task 7
cities = ["New York", "London", "Paris"]
cities.insert(0, "Tokyo")
print(cities)  

# Task 8
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  

# Task 9
prices = [10.5, 20.0, 15.75]
print(type(prices)) 

# Task 10
mixed = [10, "apple", True]
print(mixed)  

# Task 11
tuple_data = ("a", "b", "c")
list_data = list(tuple_data)
print(list_data)  

# Task 12
books = ["Python", "Java"]
books.append("JavaScript")
print(books)  

# Task 13
names = ["Alice", "Bob", "Eve"]
names.insert(1, "Charlie")
print(names)  

# Task 14
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)  

# Task 15
students = ["Alice", "Bob"]
students.extend(("Charlie", "David"))
print(students)  

# Task 16
colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)  

# Task 17
numbers = [10, 20, 30, 40]
del numbers[2]
print(numbers)  



# Task 18
fruits = ["apple", "banana", "cherry"]
fruits.clear()
print(fruits)  

# Task 19
names = ["Zoe", "Alice", "Bob"]
names.sort()
print(names)  

# Task 20
ages = [25, 35, 20]
ages.sort(reverse=True)
print(ages)  

# Task 21
words = ["Apple", "banana", "Orange"]
words.sort(key=str.lower)
print(words)  

# Task 22
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)  

# Task 23
letters = ["a", "b", "c", "d"]
print(letters[::-1])  

# Task 24
original = ["one", "two", "three"]
copy_of_original = original.copy()
print(copy_of_original)  

# Task 25
list1 = ["a", "b"]
list2 = ["c", "d"]
combined = list1 + list2
print(combined)  

# Task 26
data = [
    ["Alice", 25, ["Math", "Physics"]],
    ["Bob", 30, ["Chemistry", "Biology"]],
    ["Charlie", 35, ["History", "Geography"]]
]
print(data[0][2][1])  


# Task 27
records = [
    ["New York", [10, 20, 30]],
    ["San Francisco", [40, 50, 60]],
    ["Austin", [70, 80, 90]]
]
print(records[1][1][0])  










# SECOND ASSIGNMENT

# Initial confirmed guest list
confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"]
print("Initial Confirmed Guest List:")
print(confirmed_guests)

# Initial empty waitlist
waitlist = []


# Step 1: Adding Ken, Jack, and Ivy to the waitlist
waitlist.extend(["Ken", "Jack", "Ivy"])

print("\nAfter adding Ken, Jack, and Ivy to the waitlist:")
print(waitlist)



# Step 2: Adding Noah and Oliver to the waitlist
waitlist.extend(["Noah", "Oliver"])
print(waitlist)


# Step 3: Alice cancels, removing her from the confirmed list and add the first person from the waitlist
confirmed_guests.remove("Alice")
confirmed_guests.append(waitlist.pop(0))  # Add Ken from the waitlist to the confirmed list
print("\nAfter Alice cancels and Ken is moved from the waitlist to the confirmed list:")
print("Confirmed Guests:", confirmed_guests)
print("Waitlist:", waitlist)


# Step 4: Checking if Charlie is on the confirmed guest list

is_charlie_on_list = "Charlie" in confirmed_guests

# Print the result
print(f"\nIt is {is_charlie_on_list} that Charlie is on the confirmed guest list ")



# Step 5: David and Eve cancel their attendance
confirmed_guests.remove("David")
confirmed_guests.remove("Eve")
print("\nAfter David and Eve cancel their attendance:")
print("Confirmed Guests:", confirmed_guests)




# Moving the first 2 people from the waitlist to the confirmed guest list
confirmed_guests.extend(waitlist[:2])  # Add the first 2 people to confirmed_guests
waitlist = waitlist[2:]  # Remove the first 2 people from the waitlist

# Print the updated lists
print("\nUpdated Confirmed Guest List:")
print(confirmed_guests)

print("\nUpdated Waitlist:")
print(waitlist)






# Step 6: Oliver cancels his attendance
waitlist.remove("Oliver")
print("\nAfter Oliver cancels his attendance:")
print("Waitlist:", waitlist)

# Get the names of the last 3 guests on the confirmed guest list
last_3_guests = confirmed_guests[-3:]
print("\nLast 3 Guests on the Confirmed Guest List:")
print(last_3_guests)
