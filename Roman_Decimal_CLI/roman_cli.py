tallies = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_to_decimal(roman):
    roman = roman.upper()
    total = 0
    i = 0

    while i < len(roman):
        if i + 1 < len(roman) and tallies[roman[i]] < tallies[roman[i + 1]]:
            total += tallies[roman[i + 1]] - tallies[roman[i]]
            i += 2
        else:
            total += tallies[roman[i]]
            i += 1

    return total


def decimal_to_roman(number):
    if number == 0:
        return "N"

    negative = number < 0
    number = abs(number)

    values = [
        (1000, 'M'), (900, 'CM'),
        (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'),
        (5, 'V'), (4, 'IV'),
        (1, 'I')
    ]

    result = ""
    for value, symbol in values:
        while number >= value:
            result += symbol
            number -= value

    return "-" + result if negative else result


def is_valid_roman(roman):
    roman = roman.upper()

    if not roman:
        return False

    if any(ch not in tallies for ch in roman):
        return False

    repeat_count = 1
    prev_char = ""

    for i in range(len(roman)):
        current = roman[i]

        if current == prev_char:
            repeat_count += 1
            if current in ['V', 'L', 'D']:
                return False
            if repeat_count > 3:
                return False
        else:
            repeat_count = 1

        if i + 1 < len(roman):
            current_val = tallies[current]
            next_val = tallies[roman[i + 1]]

            if current_val < next_val:
                if current not in ['I', 'X', 'C']:
                    return False
                if next_val > current_val * 10:
                    return False

        prev_char = current

    # Reconstruct and compare for strict validation
    reconstructed = decimal_to_roman(roman_to_decimal(roman))
    return reconstructed == roman


def process_token(token):
    token = token.strip()

    if token.lower() == "exit":
        return "EXIT"

    # Decimal
    if token.lstrip('-').isdigit():
        return decimal_to_roman(int(token))

    # Roman
    if token.isalpha():
        if is_valid_roman(token):
            return str(roman_to_decimal(token))
        return "InvalidRoman"

    return "Invalid"


def main():
    print("Roman ↔ Decimal CLI Converter")
    print("Type 'exit' to stop\n")

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            print("Program stopped.")
            break

        tokens = user_input.split()
        results = []

        for token in tokens:
            result = process_token(token)

            if result == "EXIT":
                print("Program stopped.")
                return

            results.append(result)

        print("Result:", " ".join(results))


if __name__ == "__main__":
    main()