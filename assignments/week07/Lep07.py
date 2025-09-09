"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

#Code 1

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

rect = Rectangle(10, 5)
print(rect.get_area())      
print(rect.get_perimeter())  

class Circle:
    def __init__(self, radius):
        self.radius = radius
        print("Circle created!")

    def getArea(self):
        return 3.1416 * self.radius * self.radius
    
    def getPerimeter(self):
        return 2 * 3.1416 * self.radius
    
myClrcle = Circle(10)
print(myClrcle.getArea())      
print(myClrcle.getPerimeter()) 


"""
    สร้าง class Student โดยกำหนดให้
    - มี attribute ชื่อ name, age, และ student_id ที่เก็บข้อมูลทั่วไปของนักเรียน และ grades ที่เก็บคะแนนของนักเรียนในแต่ละวิชา โดยเป็นโครงสร้างข้อมูลประเภท list
    - มี method ชื่อ add_grade(subject, grade) โดย grade เป็น dictionary ที่เก็บคะแนนของนักเรียนในแต่ละวิชา
        { 
            "subject": "Mathematics", "grade": 85 
        }
    - มี method ชื่อ get_average_grade() ที่คืนค่าเฉลี่ยคะแนนของนักเรียน
    - มี method ชื่อ get_grade_report() ที่คืนค่ารายงานผลการเรียนของนักเรียน
"""

#Code 2

class Student:
    
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        sum = 0
        for grade in self.grades:
            sum += grade["grade"]
        return sum / len(self.grades)

    def get_grade_report(self):
        for grade in self.grades:
            report += f"Name: {grade["subject"]} Grade: {grade["grade"]}\n"
        return report


student = Student("John", 20, "S123")
student.add_grade(
    {
        "subject": "Math", 
        "grade": 85
    }
)
student.add_grade(
    {
        "subject": "Science",
        "grade": 92
    }
)
print(student.get_average_grade())  
print(student.get_grade_report())