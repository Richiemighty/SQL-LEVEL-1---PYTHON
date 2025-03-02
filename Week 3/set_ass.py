# 1. Check if "food" is in the set fruits
fruits = {"air", "water", "food"}
is_food_in_fruits = "food" in fruits
print(is_food_in_fruits)

# 2. Add "yellow" to colors and print the updated set
colors = {"red", "green", "blue"}
colors.add("yellow")
print(colors)

# 3. Add multiple items to animals and print the updated set
animals = {"cat", "dog", "rabbit"}
animals.update(["horse", "sheep"])
print(animals)

# 4. Remove "Canada" from countries and print the updated set
countries = {"USA", "Canada", "Mexico"}
countries.remove("Canada")
print(countries)

# 5. Remove "Houston" from cities without error
cities = {"New York", "Los Angeles", "Chicago"}
cities.discard("Houston")  # discard doesn't raise an error if item not found
print(cities)

# 6. Convert seasons list to a set to remove duplicates
seasons = ["Spring", "Summer", "Fall", "Winter", "Spring"]
unique_seasons = set(seasons)
print(unique_seasons)

# 7. Use the union method to join two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)

# 8. Find the intersection of two sets
setA = {"a", "b", "c"}
setB = {"c", "d", "e"}
intersection_set = setA.intersection(setB)
print(intersection_set)

# 9. Add 11 to prime_numbers and print the updated set
prime_numbers = {2, 3, 5, 7}
prime_numbers.add(11)
print(prime_numbers)

# 10. Remove a random item from odd_numbers and print the updated set
odd_numbers = {1, 3, 5, 7, 9}
odd_numbers.pop()  # Removes a random item
print(odd_numbers)

# 11. Empty the vowels set and print the result
vowels = {"a", "e", "i", "o", "u"}
vowels.clear()
print(vowels)

# 12. Find the difference and symmetric difference between sets
letters = {"a", "b", "c"}
another_set = {"b", "c", "d"}
difference = letters.difference(another_set)
symmetric_difference = letters.symmetric_difference(another_set)
print(difference)
print(symmetric_difference)



# 13. Add items from another set to `tech_brands` and print the updated set.
tech_brands = {"Apple", "Google", "Microsoft"}
tech_brands.update({"Amazon", "Facebook"})
print("Updated tech_brands:", tech_brands)

# 14. Remove "Charlie" from `students` and attempt to remove "Eve."
students = {"Alice", "Bob", "Charlie", "David"}
students.remove("Charlie")  # Removes "Charlie"
print("Updated students after removing 'Charlie':", students)
# Attempt to remove "Eve"
students.discard("Eve")  # Safe removal without error
print("Updated students after attempting to remove 'Eve':", students)

# 15. Convert `numbers_list` to a set to remove duplicates.
numbers_list = [1, 2, 3, 4, 4, 5, 5]
unique_numbers = set(numbers_list)
print("Unique numbers:", unique_numbers)

# 16. Convert `text` to a set to find unique characters.
text = "hello"
unique_characters = set(text)
print("Unique characters in 'hello':", unique_characters)

# 17. Find the number of items in `vehicles`.
vehicles = {"car", "bike", "bus", "train"}
vehicle_count = len(vehicles)
print("Number of items in vehicles:", vehicle_count)

# 18. Print the number of items in `gadgets`.
gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}
gadget_count = len(gadgets)
print("Number of items in gadgets:", gadget_count)





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