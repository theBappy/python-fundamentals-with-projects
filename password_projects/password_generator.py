import random
import string

def get_characters():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    return lower + upper + num + symbols

def generate_password(all_characters, password_length):
    password = "".join(random.choices(all_characters, k=password_length))
    return password

def main():
    while True:
        try:
            password_length = int(input("Enter password length (minimum 8): "))
            if password_length < 8:
                print("Your password must have at least 8 characters.")
            else:
                break
        except ValueError:
            print("Please enter numbers only.")

    all_characters = get_characters()
    password = generate_password(all_characters, password_length)
    print("\nYour password is:", password)

if __name__ == "__main__":
    main()
