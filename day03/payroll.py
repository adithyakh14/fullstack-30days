from salary_utils import calculate_gross_salary, calculate_net_salary


employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
bonus = float(input("Enter bonus: "))
deductions = float(input("Enter deductions: "))

gross_salary = calculate_gross_salary(basic_salary, bonus)
net_salary = calculate_net_salary(gross_salary, deductions)

print(f"\nEmployee: {employee_name}")
print(f"Gross Salary: Rs. {gross_salary:.2f}")
print(f"Net Salary: Rs. {net_salary:.2f}")
