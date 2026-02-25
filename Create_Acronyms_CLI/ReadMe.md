# Acronym Generator CLI

A simple Python command-line tool that converts any phrase into an acronym.

------------------------------------------------------------
FEATURES
------------------------------------------------------------

- Extracts the first letter of each word
- Converts letters to uppercase
- Removes special characters
- Ignores numbers
- Runs in continuous mode
- Type "exit" to stop
- Supports Ctrl + Z (Windows) / Ctrl + D (Mac/Linux)

------------------------------------------------------------
HOW IT WORKS
------------------------------------------------------------

1. Cleans the input
   - Removes symbols like ! @ # - _
   - Keeps letters and spaces only

2. Splits the phrase into words

3. Extracts the first letter of each valid word

4. Prints the generated acronym

5. Repeats until you stop the program

------------------------------------------------------------
INSTALLATION
------------------------------------------------------------

1. Install Python 3.x

2. Save the script as:
   acronym.py

3. Open terminal or command prompt

4. Run:
   python acronym.py

------------------------------------------------------------
USAGE EXAMPLES
------------------------------------------------------------

Input:
random access memory

Output:
Acronym: RAM


Input:
self-contained object

Output:
Acronym: SCO


Input:
123 random 456 access memory!!!

Output:
Acronym: RAM


Input:
exit

Output:
Program stopped.

------------------------------------------------------------
REQUIREMENTS
------------------------------------------------------------

- Python 3.x
- No external dependencies