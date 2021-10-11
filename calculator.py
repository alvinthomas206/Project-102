a = float(input("Enter the first number: "))
print(" ")
b = float(input("Enter the second number: "))
print(" ")

print("Enter 1 to add.")
print("Enter 2 to subtract.")
print("Enter 3 to divide.")
print("Enter 4 to multiply.")
operation = int(input("Which operation do you want ? "))

def add(a, b):
    add = a + b
    print("Answer is:","=", add)

def subtract(a,b):
    subtract = a - b
    print("Answer is: ", "=", subtract)

def divide(a, b):
    divide = a / b
    print("Answer is: ", "=", divide)

def multiply(a, b):
    multiply = a * b
    print("Answer is: ", "=", multiply)

if operation == 1:
    add(a, b)

if operation == 2:
    subtract(a, b)

if operation == 3:
    divide(a, b)

if operation == 4:
    multiply(a, b)

elif operation>=5:
    print("Enter  1, 2, 3 or 4 only.")