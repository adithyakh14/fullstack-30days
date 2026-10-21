employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
bonus_amount = float(input("Enter bonus amount: "))
deduction_amount = float(input("Enter deduction amount: "))

gross_salary = basic_salary + bonus_amount
net_salary = gross_salary - deduction_amount

print(f"Employee Name: {employee_name.strip()}")
print(f"Basic Salary: ₹{basic_salary}")
print(f"Bonus Amount: ₹{bonus_amount}")
print(f"Deduction Amount: ₹{deduction_amount}")
print(f"Gross Salary: ₹{gross_salary:,.2f}")
print(f"Net Salary: ₹{net_salary:,.2f}")