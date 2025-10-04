# Numbers to Words Converter in Python

# Lookup tables for number names
ones = (
    'Zero', 'One', 'Two', 'Three', 'Four',
    'Five', 'Six', 'Seven', 'Eight', 'Nine'
)

twos = (
    'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
    'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
)

tens = (
    'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
    'Seventy', 'Eighty', 'Ninety'
)

suffixes = (
    '', 'Thousand', 'Million', 'Billion'
)


def fetch_words(number):
    """Converts a three-digit segment into words."""
    number = number.zfill(3)  # Ensure three-digit format
    hundreds_digit = int(number[0])
    tens_digit = int(number[1])
    ones_digit = int(number[2])

    words = []
    
    if hundreds_digit > 0:
        words.append(ones[hundreds_digit])
        words.append("Hundred")

    if tens_digit > 1:
        words.append(tens[tens_digit - 2])
        if ones_digit > 0:
            words.append(ones[ones_digit])
    elif tens_digit == 1:
        words.append(twos[ones_digit])
    elif ones_digit > 0:
        words.append(ones[ones_digit])

    return " ".join(words)


def convert_to_words(number):
    """Converts a full number into words with correct suffixes."""
    str_num = str(number)
    length = len(str_num)
    
    if length > 12:
        return 'This program supports a maximum of 12-digit numbers.'

    # Split number into three-digit chunks from right to left
    num_segments = []
    while length > 0:
        num_segments.append(str_num[max(0, length - 3):length])
        length -= 3

    words = []
    for idx, segment in enumerate(num_segments):
        segment_words = fetch_words(segment)
        if segment_words:
            words.append(segment_words + (' ' + suffixes[idx] if idx > 0 else ''))

    return " ".join(reversed(words)).strip()


if __name__ == '__main__':
    number = int(input('Enter any number: '))
    print(f'{number} in words is: {convert_to_words(number)}')