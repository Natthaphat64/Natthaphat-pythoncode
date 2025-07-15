print("BMI Calculator")

weight = float(input("Weight: "))
height = float(input("Height: "))

bmi = weight / height ** 2

if bmi < 18.5:
    print("You is Underweight")
elif 
bmi >= 18.5 and <= 24.9 :
    print("You is Normal weight")
elif
bmi >= 25.0 and <= 29.9 :
    print("You is Overweight")
else:
    print("You is Obese")



direction = input("What is you")
amout = float(input("Amount to convert: "))

if direction == "1":
    result = amount / 35.5
    print("Result: ", result, "USD")

if direction == "2":
    result = amount * 35.5
    print("Result: ", result, "THB")







