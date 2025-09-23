#Code 1

import random

def test_random():
    random_number = random.randint(1, 100)

    N = int(input("What is number: "))
    if N < random_number:
        print("น้อยเกินไป") 
    elif N > random_number:
        print("มากเกินไป")
    else:
        print("เท่ากันเเล้ววว!!!")

    print(random_number)
    
test_random()


"""
Question 1: Beginner Number Guessing Game

Create a simple number guessing game with these requirements:

Random number between 1-20
    Maximum 6 attempts
    Show remaining attempts after each guess
    Display appropriate win/lose messages
    Validate numeric input only
    
Example 

    === SIMPLE GUESSING GAME ===
    Guess my number between 1 and 20!
    You have 6 attempts.

    Attempt 1/6 - Enter your guess: 10
    Too low! Try again.

    Attempt 2/6 - Enter your guess: 15
    Too high! Try again.

    Attempt 3/6 - Enter your guess: 12
    Congratulations! You won in 3 attempts!

"""

#Code 0.2 (ไม่ได้เพราะLoopไม่จบ)
import random

def test_random():
    random_number = random.randint(1, 20)

    N = int(input("What is number: "))
    while True:
        if N < random_number:
            print("น้อยเกินไป") 
        elif N > random_number:
            print("มากเกินไป")
        else:
            print("เท่ากันเเล้ววว!!!")
    
test_random()

#Code 2 
import random

print("=== SIMPLE GUESSING GAME ===")
print("Guess my number between 1 and 20!")
print(f"You have 6 attempts.")

random_number = random.randint(1, 20)

for i in range(6):
    guess_number = int(input(f"Attempts {i+1}/6 - Enter your guess:"))

    if random_number == guess_number:
        print(f"Congratulations! You won in {i+1} attempts")
        break
    elif random_number < guess_number:
        print("Too high! Try again.")
    else:
        print("Too low! try again.")


"""
#Question 2: Enhanced Guessing Game with Hints
Develop an enhanced guessing game with intelligent hint system:
Core Features:

Random number between 1-100
Unlimited attempts

Progressive hint system:

    After 3 wrong guesses: Show if number is odd/even
    After 5 wrong guesses: Show if divisible by 3 or 5
    After 7 wrong guesses: Narrow the range to 25-number window
    After 10 wrong guesses: Show first digit
    
Example 
    === Enhanced GUESSING GAME ===
    Guess my number between 1 and 100!
    You have unlimited attempts.

    Attempt 1 - Enter your guess: 10
    Too low! Try again.

    Attempt 2 - Enter your guess: 15
    Too high! Try again.

    Attempt 3 - Enter your guess: 12
    Too low! Try again.
    HINT: The number is even
    
    ...
    
    Attempt 5 - Enter your guess: 20
    Too high! Try again.
    HINT: The number is divisible by 5
    
    ...
    
    Congratulations! You won in 10 attempts!

"""

#Code 3
import random

def get_parity_hint(number):
    if number % 2 == 0:
        return "HINT: The number is even" 
    else:
        return "HINT: The number is odd"

def get_divisibility_hint(number):
    if number % 3 == 0:
        return "HINT: The number is divisible by 3"
    elif number % 5 == 0:
        return "HINT: The number is divisible by 5"
    else:
        return "HINT: The number is NOT divisible by 3 or 5"

def get_range_hint(number, current_min=1, current_max=100):
    # Return narrowed range around the number
    return f"HINT: The narrowed range arount the number is {range(number - 12,number + 12)}"

def get_thefirst_digit_hint(number):
    # Retun the first digit of the number
    first_digit = number // 10
    return f"HINT: The first digit if {first_digit}"

random_number = random.randint(1, 100)
attempt = 1

while True:
    guess_number = int(input(f"Attempts {attempt} - Enter your guess:"))

    if random_number == guess_number:
        print(f"Congratulations! You won in {attempt} attempts")
        break
    elif random_number < guess_number:
        print("Too high! Try again.")
    else:
        print("Too low! try again.")

    if attempt == 3:
        print(get_parity_hint(random_number))
    elif attempt == 5:
        print(get_divisibility_hint(random_number))
    elif attempt == 7:
        print(get_range_hint(random_number))
    elif attempt == 10:
        print(get_thefirst_digit_hint(random_number))
    
    attempt = attempt + 1