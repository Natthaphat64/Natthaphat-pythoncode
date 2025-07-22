# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:

# Code 1
age = int(input("Enter age: "))
if age <= 12:
    print("You age is Child")
elif age >= 13 and age <= 19:
    print("You age is Teenager")
elif age >= 20 and age <= 59:
    print("You age is Adult")
else:
    print("You age is Senior")


# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        # Complete the menu logic here
        # Your code here:
        
else:
    print("Invalid PIN")


#Code 2
("ATM")
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
while True:
    print("\n=== Main Menu ===")
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit") 
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        print("You balance = ",balance)

    if choice == "2":
        amount = float(input("withdraw amount: "))
        if amount < 0:
            print("Cannot withdraw less than 0")
        else:
            balance = balance - amount
            print("Plase collect your maney,and your balance now = ",balance)

    if choice == "3":
        amount = float(input(": Deposit amount: "))
        if amount < 0:
            print("Cannot deposit less than 0")
        else:
            balance = balance + amount
            print("Your balance now = ",balance)
    if choice == "4":
        break
    else:
        continue
else:
    print("Invalid PIN")


