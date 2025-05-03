# Function for sum
def sum(a, b):
    c = a + b
    return c

# Function for sub
def sub(a, b):
    c = a - b
    return c

# Function for multiply
def mul(a, b):
    c = a * b
    return c

# Function for divide
def div(a, b):
    c = a / b
    return c

# Function for get remainder
def rem(a, b):
    c = a % b
    return c

# First number input
try:
    num1 = int(input("Enter first number: "))
except ValueError:
    print("----Invalid Input----")
    exit()

# Choice print
print("Please select option:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Remainder")

# Choice input
try:
    choice = int(input("Enter your choice: "))
except ValueError:
    print("----Invalid Input----")
    exit()

# Second number input
try:
    num2 = int(input("Enter second number: "))
except ValueError:
    print("Invalid input")
    exit()

# Match case statement for choice
match choice:
    case 1:
        c = sum(num1, num2)
        print(f"Addition of these numbers is {c}")
    case 2:
        c = sub(num1, num2)
        print(f"Subtraction of these numbers is {c}")
    case 3:
        c = mul(num1, num2)
        print(f"Multiplication of these numbers is {c}")
    case 4:
        try:
            c = div(num1, num2)
            print(f"Division of these numbers is {c}")
        except ZeroDivisionError:
            print("Not divided by zero")
    case 5:
        try:
            c = rem(num1, num2)
            print(f"Remainder is {c}")
        except ZeroDivisionError:
            print("Cannot find remainder with zero as divisor")
    case _:
        print("---Invalid choice---")
        print("---Enter valid choice---")

print("-----Thank You----")
