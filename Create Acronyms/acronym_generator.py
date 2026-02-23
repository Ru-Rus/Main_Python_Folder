# Acronym_Generator -Python Code
import re


def generate_acronym(phrase: str) -> str:
    # Remove special characters (keep letters and spaces only)
    cleaned = re.sub(r'[^A-Za-z\s]', '', phrase)

    words = cleaned.split()

    # Ignore words that are purely numeric (extra safety)
    words = [word for word in words if not word.isdigit()]

    return "".join(word[0].upper() for word in words if word)


def main():
    while True:
        try:
            user_input = input("Enter a Phrase (type 'exit' to quit): ").strip()

            if user_input.lower() == "exit":
                print("Program stopped.")
                break

            if not user_input:
                print("No Input")
                continue

            acronym = generate_acronym(user_input)

            if acronym:
                print("Acronym:", acronym)
            else:
                print("No valid words found.")

        except EOFError:
            print("\nProgram stopped.")
            break


if __name__ == "__main__":
    main()