import re

def test_password_strength(password):
    eight_char_long = re.compile(r"[\w\d\s\W\D\S]{8,}")
    upper_case_regex = re.compile(r"[A-Z]+")
    lower_case_regex = re.compile(r"[a-z]+")
    one_or_more_digit_regex = re.compile(r"\d+")

    if not eight_char_long.search(password):
        return False
    elif not upper_case_regex.search(password):
        return False
    elif not lower_case_regex.search(password):
        return False
    elif not one_or_more_digit_regex.search(password):
        return False
    
    return True

if __name__ == "__main__":
    password = input("Enter password: ")
    print(test_password_strength(password))
