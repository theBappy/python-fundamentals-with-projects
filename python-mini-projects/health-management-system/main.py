import datetime


def get_time():
    return datetime.datetime.now()


def input_t(n):
    if n == 1:
        d = int(input("Enter 1 for exerise and 2 for food :"))
        if d == 1:
            value = input("type here.. \n")
            with open("david-exe.txt", "a") as op:
                op.write(str([str(get_time())]) + ": " + value + "\n ")
            print("written successfully ")
        elif d == 2:
            value = input("type here.. \n")
            with open("david-food.txt", "a") as op:
                op.write(str([str(get_time())]) + ": " + value + "\n ")
            print("written successfully ")
    elif n == 2:
        d = int(input("Enter 1 for exercise and 2 for food :"))
        if d == 1:
            value = input("type here.. \n")
            with open("john-exe.txt", "a") as op:
                op.write(str([str(get_time())]) + ": " + value + "\n ")
            print("written successfully ")
        elif d == 2:
            value = input("type here.. \n")
            with open("john-food.txt", "a") as op:
                op.write(str([str(get_time())]) + ": " + value + "\n ")
            print("written successfully ")
    elif n == 3:
        d = int(input("Enter 1 for exercise and 2 for food :"))
        if d == 1:
            value = input("type here.. \n")
            with open("john-exe.txt", "a") as op:
                op.write(str([str(get_time())]) + ": " + value + "\n ")
            print("written successfully ")
        elif d == 2:
            value = input("type here.. \n")
            with open("john-food.txt", "a") as op:
                op.write(str([str(get_time())]) + ": " + value + "\n ")
            print("written successfully ")
    else:
        print("Enter the valid input 1(david) 2(john) 3(john)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("david-exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("david-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 2:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("john-exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("john-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif k == 3:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("john-exe.txt") as op:
                for i in op:
                    print(i, end="")
        elif c == 2:
            with open("john-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (david,john,john)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for david 2 for john 3 for john "))
    input_t(b)
else:
    b = int(input("Press 1 for david 2 for john 3 for john "))
    retrieve(b)