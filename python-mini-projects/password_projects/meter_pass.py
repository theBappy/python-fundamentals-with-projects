import string

# Global variables
acentos = "áéíóúàèìòùäëïöüâêîôûñç"
exceptions = "_ "
sequenceNumbers = "0123456789"
sequenceAlphabet = string.ascii_lowercase

# ----- 1. Basic Character Bonuses -----
def numberOfCharacters(password):
    return len(password) * 4


def upperCaseLetters(password):
    charsUpper = sum(1 for i in password if i.isupper())
    if charsUpper > 0:
        return (len(password) - charsUpper) * 2
    return 0


def lowerCaseLetters(password):
    charLower = sum(1 for i in password if i.islower() and i not in acentos)
    if charLower > 0:
        return (len(password) - charLower) * 2
    return 0


def numbers(password):
    charsNumber = sum(1 for i in password if i.isdigit())
    if charsNumber > 0 and not password.isdigit():
        return charsNumber * 4
    return 0


def symbols(password):
    charsSymbol = sum(
        1
        for i in password
        if i.lower() not in sequenceAlphabet
        and i not in exceptions
        and i not in sequenceNumbers
    )
    return charsSymbol * 6


def middleNumberOrSymbol(password):
    charMiddle = 0
    for i in range(1, len(password) - 1):
        if password[i].isdigit() or (
            password[i].lower() not in sequenceAlphabet
            and password[i] not in exceptions
        ):
            charMiddle += 1
    return charMiddle * 2


# ----- 2. Requirements -----
def requirements(password):
    requirementCount = 0

    if len(password) >= 8:
        requirementCount += 1
    if upperCaseLetters(password) > 0:
        requirementCount += 1
    if lowerCaseLetters(password) > 0:
        requirementCount += 1
    if numbers(password) > 0:
        requirementCount += 1
    if symbols(password) > 0:
        requirementCount += 1

    if requirementCount >= 4:
        requirementCount *= 2  # bonus
    return requirementCount


# ----- 3. Penalty Rules -----
def lettersOnly(password):
    if any(ch.isdigit() for ch in password):
        return 0
    return len(password) * (-1)


def numbersOnly(password):
    if any(ch.isalpha() for ch in password):
        return 0
    return len(password) * (-1)


def consecutiveLowerCase(password):
    countLowerCase = 0
    password += "1"  # avoid index error
    for i in range(len(password) - 1):
        if (
            password[i].islower()
            and password[i + 1].islower()
            and password[i + 1] not in acentos
            and password[i] not in acentos
        ):
            countLowerCase += 1
    return countLowerCase * (-2)


def consecutiveUpperCase(password):
    countUpperCase = 0
    password += "1"
    for i in range(len(password) - 1):
        if password[i].isupper() and password[i + 1].isupper():
            countUpperCase += 1
    return countUpperCase * (-2)


def consecutiveNumbers(password):
    countNumbers = 0
    password += "a"
    for i in range(len(password) - 1):
        if password[i].isdigit() and password[i + 1].isdigit():
            countNumbers += 1
    return countNumbers * (-2)


def sequentialNumbers(password):
    sequenceThreeDigitNumbers = [
        "012", "123", "234", "345", "456", "567", "678", "789", "890"
    ]
    countNumbers = 0
    for i in range(len(password) - 2):
        numbers = password[i:i + 3]
        if numbers in sequenceThreeDigitNumbers:
            countNumbers += 1
    return countNumbers * (-3)


def sequentialLetters(password):
    sequenceThreeAlphabet = [
        "abc", "bcd", "cde", "def", "efg", "fgh", "ghi",
        "hij", "ijk", "jkl", "klm", "lmn", "mno", "nop",
        "opq", "pqr", "qrs", "rst", "stu", "tuv", "uvw",
        "vwx", "wxy", "xyz"
    ]
    countLetters = 0
    for i in range(len(password) - 2):
        letters = password[i:i + 3]
        if letters.lower() in sequenceThreeAlphabet:
            countLetters += 1
    return countLetters * (-3)


# ----- 4. Aggregate Function -----
def passwordStrength(password):
    score = 0
    score += numberOfCharacters(password)
    score += upperCaseLetters(password)
    score += lowerCaseLetters(password)
    score += numbers(password)
    score += symbols(password)
    score += middleNumberOrSymbol(password)
    score += requirements(password)
    score += lettersOnly(password)
    score += numbersOnly(password)
    score += consecutiveLowerCase(password)
    score += consecutiveUpperCase(password)
    score += consecutiveNumbers(password)
    score += sequentialNumbers(password)
    score += sequentialLetters(password)

    return score

# ----- 6. Password grading -----
def passwordGrade(score):
    if score >= 80:
        return "Very Strong"
    elif score >= 60:
        return "Strong"
    elif score >= 40:
        return "Moderate"
    elif score >= 20:
        return "Weak"
    else:
        return "Very Weak"


# ----- 7. Example Run -----
if __name__ == "__main__":
    password = input("Enter password to evaluate: ")
    strength = passwordStrength(password)
    grade = passwordGrade(strength)

    print(f"\nPassword strength score: {strength}")
    print(f"Password grade: {grade}")
