"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

#Code 1

print("=== PERSONAL INFORMATION VALIDATOR ===")

name = input("Enter your name: ")
age = input("Enter your age: ")
phone_number = input("Enter your phone number: ")

nameFlag = True

for char in name:
    if char.isalpha() or char == " ":
        nameFlag = True
    
    else:
        nameFlag = False
    
ageFlag = True
if int(age) < 18 or int(age) > 65:
    ageFlag = False

phoneFlag = True
if len(phone_number) != 10:
    phoneFlag = False
else:
    for char in phone_number:
        if char.isdigit == False:
            phoneFlag = False
            break

print("\nValidation Results: ")
if nameFlag:
    print("Name: Valid(contains only letters and spaces)")
else:
    print("Name : Invalid (not contains only letters and spaces)")

if ageFlag:
    print(f"Age: Valid ({age} years old)")
else:
    print("Age: Invalid (less than 18 or more then 65)")

if phoneFlag:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (not 10-digit number)")

print("\nFormatted Information: ")
print("Name:",name.upper(), name.lower(), name.capitalize(), name.title())
if int(age) >= 18 and int(age) <= 30:
    print("Age Group: Young Adult (18-30)")
else:
    print("Age Group: not Young Adult")

print("Phone: +66-%s" % phone_number)


"""

Build a Text Analysis Tool that performs the following operations on user input text:
Core Features:

1. Character Analysis:
    - Count total characters (with and without spaces)
    - Count vowels and consonants separately
    - Find most frequent character

2. Word Analysis:
    - Count total words
    - Find longest and shortest words
    - Count words starting with vowels vs consonants

3. String Transformations:
    - Convert to title case, upper case, lower case
    - Create acronym from first letter of each word
    - Reverse the entire string and each word individually
    
Example Result

Enter text: The Quick Brown Fox Jumps Over The Lazy Dog

=== TEXT ANALYSIS REPORT ===
Character Analysis:
- Total characters: 43 (with spaces), 35 (without spaces)
- Vowels: 12 (e, u, i, o, o, u, o, e, e, a, o)
- Consonants: 23
- Most frequent: 'o' (appears 4 times)

Word Analysis:
- Total words: 9
- Longest word: "Quick" (5 letters)
- Shortest word: "The" (3 letters)
- Words starting with vowels: 1 ("Over")
- Words starting with consonants: 8

Transformations:
- Title Case: The Quick Brown Fox Jumps Over The Lazy Dog
- Upper Case: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
- Lower Case: the quick brown fox jumps over the lazy dog
- Acronym: TQBFJOTLD
- Reversed Text: goD yzaL ehT revO spmuJ xoF nworB kciuQ ehT
- Words Reversed: ehT kciuQ nworB xoF spmuJ revO ehT yzaL goD

USE: len(), split(), count(), upper(), lower(), title(), slicing operations

"""

#Code 2

string = "The Quick Brown Fox Jumps Over The Lez"

print("=== TEXT ANALYSIS TOOL ===")
print("Character Analysis: ")
print("- Total charcters: %d (with spaces), %d (without spaces)" % (len(string), len(string)-string.count(" ")))

strLower = string.lower()
vowels = strLower.count("a") + strLower.count("e") + strLower.count("i") + strLower.count("o") + strLower.count("u")
vowelsStr = ""
for char in strLower:
    if char in ['a', 'e', 'i', 'o', 'u']:
        vowelsStr += char + ","

print("- Vowels: %d (%s)" % (vowels, vowelsStr))
print("- Consonants: %d" % (len(string)-string.count(" ")-vowels))

words = string.split()
print("- Total words:",len(words))