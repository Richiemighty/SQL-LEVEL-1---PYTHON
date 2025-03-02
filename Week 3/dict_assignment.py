
# Task 1: Creating and accessing a dictionary
student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])  # Output: John

# Task 2: Modifying a dictionary value
product = {"name": "Laptop", "price": 999.99, "stock": 50}
product["price"] = 899.99
print(product)

# Task 3: Adding a new key-value pair
employee = {"name": "Alice", "position": "Manager"}
print(f"Before: {employee}")
employee["salary"] = 50000
print(f"After: {employee}")



# Task 4: Removing a key from a dictionary
inventory = {"apple": 10, "banana": 5, "orange": 8}
print(f"Before: {inventory}")
del inventory["banana"]
print(f"After: {inventory}")



# Task 5: Copying a dictionary
person = {"name": "Bob", "age": 25, "city": "New York"}
# print(f"Before: {person}")
person_copy = person.copy()
print(f"person copy: {person_copy}")


# Task 6: Accessing a nested dictionary
family = {
    "child1": {"name": "Tom", "age": 10},
    "child2": {"name": "Lucy", "age": 8},
    "child3": {"name": "Anna", "age": 5}
}
print(family["child2"]["age"]) 

# Task 7: Accessing a dictionary value
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
print(car["model"])  

# Task 8: Changing a value in a dictionary
settings = {"volume": 50, "brightness": 75, "language": "English"}
print(f"Before: {settings}")
settings["language"] = "Spanish"
print(f"After: {settings}")



# Task 9: Removing a key from a dictionary
scores = {"math": 90, "science": 85, "english": 88}
print(f"Before: {scores}")
del scores["science"]
print(f"After: {scores}")


# Task 10: Checking for a key in a dictionary
menu = {"starter": "Soup", "main_course": "Steak", "dessert": "Ice Cream"}
print("appetizer" in menu)  

# Task 11: Clearing a dictionary
config = {"theme": "dark", "language": "English", "timezone": "UTC"}
config.clear()
print(config)



# Task 12: Creating a dictionary and printing the number of items
phone_book = {"Alice": "1234567890", "Bob": "2345678901", "Charlie": "3456789012"}
# print(f"Before: {phone_book}")
print(f"Number of items: {len(phone_book)}")

# Task 13: Creating a dictionary and getting a list of keys
grades = {"math": "A", "science": "B", "history": "C"}
print(f"\nBefore: {grades}")

keys_list = list(grades.keys())

print(f"List of keys: {keys_list}")


# Task 14: Creating a dictionary and getting a list of values
employee = {"name": "David", "position": "Engineer", "salary": 70000}
print(f"\nBefore: {employee}")
values_list = list(employee.values())
print(f"List of values: {values_list}")

# Task 15: Creating a dictionary and getting a list of key-value pairs
game = {"title": "Minecraft", "genre": "Sandbox", "rating": 4.5}
print(f"\nBefore: {game}")
items_list = list(game.items())
print(f"List of key-value pairs: {items_list}")























#### TUPLE ASSIGNMENT

# Task 1: Unpacking dimensions
dimensions = (10, 20, 30)
length, width, height = dimensions
print(f"Length: {length}, Width: {width}, Height: {height}")


# Task 2: Unpacking coordinates
coordinates = (1.5, 2.5, 3.5)
x, y, z = coordinates
print(f"Y: {y}")


# Task 3: Unpacking person tuple
person = ("John", 25, "Engineer")
name, age, profession = person
print(f"Profession: {profession}")


# Task 4: Unpacking nested tuple data
data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
(student1, student2), subjects, scores = data
print(f"Student2: {student2}")


# Task 5: Unpacking colors
colors = ("red", "green", "blue", "yellow")
color1, color2, *_ = colors
print(f"Color1: {color1}, Color2: {color2}")


# Task 6: Unpacking record tuple
record = ("Jane", (32, "Manager"), ["HR", "Finance"])
name, (age, position), departments = record
print(f"Age: {age}, First Department: {departments[0]}")



# Task 7: Unpacking triplet
triplet = ("one", "two", "three")
first, second, third = triplet
print(f"Second Variable: {second}")



# Task 8: Unpacking info tuple
info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
product_id, (category, price), (day, month, year) = info
print(f"Category: {category}, Manufacture Year: {year}")



# Task 9: Unpacking nested_tuple
nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
first, second, third = nested_tuple
print(f"Second Value of Third Tuple: {third[1]}")




# Task 10: Unpacking inventory tuple
inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
(fruit1, quantity1), (fruit2, quantity2), (fruit3, quantity3) = inventory
print(f"Quantity of Bananas: {quantity2}")