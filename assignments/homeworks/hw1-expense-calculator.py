"""
Personal Finance Calculator
Student: Natthapat Supaphol
Date: 23 July 2025
Purpose: Calculate monthly budget and savings
"""

# รับค่าใช้จ่าย-รายได้
monthly_income = float(input("Enter your monthly income (THB): "))  # รายได้ต่อเดือน
rent_cost = float(input("Enter your rent cost (THB): "))  # ค่าที่พัก
food_budget = int(input("Enter your food budget (THB): "))  # ค่ากิน
transportation_cost = float(input("Enter your transportation cost (THB): "))  # ค่าเดินทาง
entertainment_budget = int(input("Enter your entertainment budget (THB): "))  # ค่าพักผ่อน
emergency_fund_percent = float(input("Enter emergency fund percent (e.g. 10.5): "))  # เงินสำรอง
investment_percent = float(input("Enter investment percent (e.g. 15.0): "))  # เงินลงทุน

# คำนวณค่าใช้จ่าย
fixed_expenses = rent_cost + transportation_cost  # ค่าใช้จ่ายคงที่ = ค่าที่พัก + ค่าเดินทาง
variable_expenses = food_budget + entertainment_budget  # ค่าใช้จ่ายไม่คงที่ = ค่ากิน + พักผ่อน
total_expenses = fixed_expenses + variable_expenses  # รวมค่าใช้จ่าย
remaining_income = monthly_income - total_expenses  # รายได้คงเหลือ
emergency_fund = monthly_income * (emergency_fund_percent / 100)  # เงินฉุกเฉิน
investment_amount = monthly_income * (investment_percent / 100)  # เงินลงทุน
available_for_savings = remaining_income - emergency_fund - investment_amount # เงินเหลือสำหรับออม
expense_ratio = (total_expenses / monthly_income) * 100 # สัดส่วนค่าใช้จ่าย

# แสดงผล
print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {fixed_expenses:.2f} THB")
print(f"Variable Expenses: {variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent:.0f}%): {emergency_fund:.2f} THB")
print(f"Investment ({investment_percent:.0f}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")
