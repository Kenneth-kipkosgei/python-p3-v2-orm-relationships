#!/usr/bin/env python3

import sys
sys.path.append('lib')

from __init__ import CONN, CURSOR
from department import Department
from employee import Employee

def test_relationship():
    # Reset database
    Employee.drop_table()
    Department.drop_table()
    Department.create_table()
    Employee.create_table()

    # Create departments
    payroll = Department.create("Payroll", "Building A, 5th Floor")
    hr = Department.create("Human Resources", "Building C, East Wing")
    
    # Create employees
    Employee.create("Amir", "Accountant", payroll.id)
    Employee.create("Bola", "Manager", payroll.id)
    Employee.create("Charlie", "Manager", hr.id)
    Employee.create("Dani", "Benefits Coordinator", hr.id)
    
    print("=== All Departments ===")
    for dept in Department.get_all():
        print(dept)
    
    print("\n=== All Employees ===")
    for emp in Employee.get_all():
        print(emp)
    
    print("\n=== Payroll Department Employees ===")
    payroll_employees = payroll.employees()
    for emp in payroll_employees:
        print(emp)
    
    print("\n=== HR Department Employees ===")
    hr_employees = hr.employees()
    for emp in hr_employees:
        print(emp)
    
    print("\n=== Employee to Department Lookup ===")
    employee = Employee.find_by_id(1)
    department = Department.find_by_id(employee.department_id)
    print(f"Employee: {employee}")
    print(f"Works in: {department}")

if __name__ == "__main__":
    test_relationship()