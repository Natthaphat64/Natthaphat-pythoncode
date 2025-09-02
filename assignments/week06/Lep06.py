""" เขียน function ชื่อ welcome_message ที่มีคุณสมบัติดังนี้:

รับ parameter 2 ตัว คือ name และ course
return ข้อความต้อนรับในรูปแบบ string
รูปแบบ: "Welcome [name] to [course] class!"

"""

#Code 1

def welcome_message(name, course):
    return f"Welcome {name} to {course} class!"

print(welcome_message("Nat", "Python"))
print(welcome_message("Pat", "Com"))


""" เขียน function ชื่อ calculate_circle ที่มีคุณสมบัติดังนี้:

รับ parameter 1 ตัว คือ radius
return dictionary ที่มี area และ circumference
ใช้ค่า π = 3.14159
ปัดเศษทั้งสองค่าให้เหลือ 2 ตำแหน่งหลังจุดทศนิยม """

#Code 2

def calculate_circle(radius):
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return {"area": round(area,2),
            "circumference": round(circumference, 2)
    }
print()


""" เขียน function ชื่อ create_user_profile ที่มีคุณสมบัติดังนี้:

รับ parameters: username (จำเป็น), age (ค่าเริ่มต้น 18), premium (ค่าเริ่มต้น False)
return string ที่จัดรูปแบบข้อมูลผู้ใช้
รูปแบบ: "[username] (age: [age]) - [Premium User / Standard User]"

"""

#Code 3

def create_user_profile(username, age=18, premium=False):
    if premium :
        return f"{username} (age:{age}) - Premium User"
    else:
        return f"{username} (age:{age}) - Standard User"
    

""" เขียน function ชื่อ analyze_scores ที่มีคุณสมบัติดังนี้:

รับ list ของคะแนน (ตัวเลข)
return dictionary ที่มี:

total: ผลรวมของคะแนนทั้งหมด
average: คะแนนเฉลี่ย (ปัดเศษ 1 ตำแหน่งหลังจุดทศนิยม)
highest: คะแนนสูงสุด
lowest: คะแนนต่ำสุด
passed: จำนวนคะแนนที่ >= 70 """

#Code 4

def analyze_scores(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    lowest = min(numbers)
    highest = max(numbers)

    morethan70 = 0
    for number in numbers:
        if number >= 70:
            morethan70 += 1;

    return {
        'sum': total,
        'count': count,
        'average': round(average, 2),
        'minimum': lowest,
        'maximum': highest,
        'passed': morethan70 
    }


""" เขียน function ชื่อ count_vowels_consonants ที่มีคุณสมบัติดังนี้:

รับ parameter text เป็น string
นับสระ (a, e, i, o, u) และพยัญชนะ (ไม่นับช่องว่างและตัวเลข)
return dictionary ที่มี vowels และ consonants counts
ไม่สนใจตัวใหญ่ตัวเล็ก (case insensitive) """

#Code 5

def count_vowels_consonants(text):
    text.lower(text)
    text.replace("","")
    text.replace("0","")
    text.replace("1","")
    text.replace("2","")
    text.replace("3","")
    text.replace("4","")
    text.replace("5","")
    text.replace("6","")
    text.replace("7","")
    text.replace("8","")
    text.replace("9","")

    vowels = text.count('a') + text.count('e') + text.count('i') + text.count('o') + text.count('u')
    consonants = len(text) - vowels

    return {
        "vowels": vowels,
        "consonants": consonants
    }