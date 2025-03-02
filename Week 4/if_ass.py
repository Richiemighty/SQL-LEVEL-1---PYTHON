# 1. Check positivity of a and b
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
if a > 0 and b > 0:
    print("a and b are both positive")
elif a > 0 or b > 0:
    print("Only one is positive")
else:
    print("Neither is positive")




# 2. Check order of x, y, z
x, y, z = map(int, input("Enter three numbers (x, y, z) separated by commas: ").split(','))
if x < y < z:
    print("Increasing order")
elif x > y > z:
    print("Decreasing order")
else:
    print("Neither")





# 3. Check if a string is a palindrome
palindrome = input("Enter a string: ").replace(" ", "")
if palindrome.lower() == palindrome[::-1].lower():
    print("Is a palindrome")
else:
    print("Not a palindrome")


# 4. Check equality of x, y, z
x = int(input("Enter first number (x): "))
y = int(input("Enter second number (y): "))
z = int(input("Enter third number (z): "))

if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
    print("Two are equal")
elif x == y == z:
    print("All same")
else:
    print("All different")


# OR 

# Collect inputs
x = input("Enter the first value (x): ")
y = input("Enter the second value (y): ")
z = input("Enter the third value (z): ")

# Store the values in a list and count unique values using a set
values = [x, y, z]
unique_values = len(set(values))

# Check conditions based on the number of unique values
if unique_values == 2:
    print("Two are equal")
elif unique_values == 1:
    print("All same")
else:
    print("All different")





# 5. Check for valid triangle
angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))
angle3 = int(input("Enter third angle: "))

if (angle1 > 0 and angle2 > 0 and angle3 > 0) and (angle1 + angle2 + angle3 == 180):
    print("Valid triangle")
else:
    print("Invalid triangle")


# 6. Check if character is a vowel
ch = input("Enter a character: ").lower()
if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")




import string
ch = input("Enter a character: ").lower()
alphabet = string.ascii_lowercase
if ch in "aeiou":
    print("Vowel")
elif ch in alphabet:
    print("Consonant")
else:
    print("Not and Alphabet")


# 7. Check if colors are primary
color1, color2, color3 = input("Enter three colors separated by commas: ").split(',')
primary_colors = ["red", "blue", "yellow"]

if color1.strip().lower() in primary_colors and color2.strip().lower() in primary_colors and color3.strip().lower() in primary_colors:
    print("All primary colors")
else:
    print("Not all primary colors")



# 8. Check system mode
mode = input("Enter system mode (manual, automatic, off): ").lower()
if mode == "manual":
    print("Manual mode activated")
elif mode == "automatic":
    print("Automatic mode activated")
elif mode == "off":
    print("System is off")
else:
    print("Invalid mode")


# 9. Check for high priority message
message = input("Enter a message: ").lower()
if any(word in message for word in ["urgent", "important", "immediate"]):
    print("High priority message")
else:
    print("Normal message")


# 10. Check activity statuses
status1 = input("Enter status1 (active/inactive/pending): ").lower().strip()
status2 = input("Enter status2 (active/inactive/pending): ").lower().strip()
if status1 == "active" and status2 == "active":
    print("Both active")
elif status1 == "active" or status2 == "active":
    print("One active")
else:
    print("None active")

# 11. Check for image file extension
filename = input("Enter a filename: ").lower()
if filename.endswith((".jpg", ".png", ".gif")):
    print("Image file")
else:
    print("Not an image file")

# 12. Access levels
access_level = input("Enter access level (admin/user/guest): ").lower()
if access_level == "admin":
    print("Full access")
elif access_level == "user":
    print("Limited access")
elif access_level == "guest":
    print("No access")

# 13. Validate email
email = input("Enter an email: ")
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")

# 14. Check if day is weekday or weekend
day = input("Enter a day of the week: ").capitalize().strip(" ")
if day in ["Saturday", "Sunday"]:
    print("Weekend")
else:
    print("Weekday")

# 15. Find the greatest number
num1, num2, num3 = map(float, input("Enter three numbers separated by commas: ").split(','))
greatest = max(num1, num2, num3)
print(f"The greatest number is: {greatest}")