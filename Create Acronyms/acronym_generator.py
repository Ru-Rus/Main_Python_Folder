# Acronym_Generator -Python Code
while True:
    try:
        user_input = input("Enter a Phrase: ").strip()
        
        text = user_input.split()
        a = ""

        if len(text) > 0:
            for word in text:
                a += word[0].upper()
            print("Acronym:", a)
        else:
            print("No Input")

    except EOFError:
        print("\nProgram stopped.")
        break