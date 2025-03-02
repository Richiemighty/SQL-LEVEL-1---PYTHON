# class Richie():
#     def __init__(self):
#         self.name = 'richie'
#         print(self.name)
#         self.myname()
    
#     def myname(self):
#         print(f"My name is {self.name.upper()}")

# Richie()

x = 5
y = 4

class Math():
    def __init__(self, num1 , num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print(f"{self.num1} + {self.num2} = {self.num1 + self.num2}")
        
    def sub(self):
        print(f"{self.num1} - {self.num2} = {self.num1 - self.num2}")

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
choice = input("What operation do you want to perform? ")

m = Math(num1, num2)

if choice.strip().lower() == 'addition':
    m.add()
elif choice.strip().lower() == 'subtraction':
    m.sub()
    






