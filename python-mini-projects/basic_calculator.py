
# define the function needed, add, sub, mul, div
# print options to the users

def add(a,b):
    answer = a + b
    print(f"a + b = {answer}")
def sub(a,b):
    answer = a - b
    print(f"a - b = {answer}")
def mul(a, b):
    answer = a * b 
    print(f"a * b = {answer}")
def div(a,b):
    answer = a / b
    print(f"a / b = {answer}")

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    choice = input("Enter your choice: ")

    if choice.lower() == 'a':
        print("Addition")
        a = int(input("Enter the a: "))
        b = int(input("Enter the b: "))
        add(a, b)
    elif choice.lower() == 'b':
        print("Addition")
        a = int(input("Enter the a: "))
        b = int(input("Enter the b: "))
        sub(a, b)
    elif choice.lower() == 'c':
        print("Addition")
        a = int(input("Enter the a: "))
        b = int(input("Enter the b: "))
        mul(a, b)
    elif choice.lower() == 'd':
        print("Addition")
        a = int(input("Enter the a: "))
        b = int(input("Enter the b: "))
        div(a, b)
    elif choice.lower() == "e":
        print("Program ended")
        quit()