
"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

#Code 1

def personal_info_manager():
    person = ("Natthaphat", 19, "Chonburi", "TH") 
    hobbies = []

    while True:

        choice = input("What do you want to do? (1: Display, 2: Add hoppy, 3: Remove hoppy, 4: Edit age, 5: Exid): ")

        if choice == "1":
            print("Name: ", person[0])
            print(f"Age: {person[1]}")
            print("City: " + person[2])
            print("Country: ", person[3])
            print("Hobbies: ", hobbies)

        elif choice == "2":
            hobby = input("What is your new hobbies: ")
            hobbies.append(hobby)

        elif choice == "3":
            hobbies.pop()

        elif choice == "4":
            person_list = list(person)
            age = input("How old are you?: ")
            person_list[1] = age
            person = tuple(person_list)

        elif choice == "5":
            break

if __name__ == "__main__":
    personal_info_manager()

"""
Number List Operations

Ask user to input 10 numbers and store them in a list
Display the original list

Create and display:

List of even numbers
List of odd numbers
List of numbers greater than the average


Show statistics: sum, average, min, max

"""

#Code 2

def number_operations():
    numbers = []
    
    print("Enter 10 numbers:")
    for i in range(10):
        number = int(input("Insert number [" + i + "]: "))
        numbers.append(number)
    
    print(f"Original numbers: {numbers}")
    
    even_numbers = []
    odd_numbers = []
    average = sum(numbers) / 10.0
    above_average = []

    for i in range(10):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
        else:
            odd_numbers.append(numbers[i])

        if numbers[i] > average:
            above_average.append(number[i])

    print("Even Number List: ",even_numbers)
    print("Odd Number List: ",odd_numbers)
    print("Above Average List: ",above_average)
    print("Sum: ",sum(number))
    print("Averge: ",average)
    print("Min: ",min(numbers))
    print("Max: ",max(numbers))
    
if __name__ == "__main__":
    number_operations()