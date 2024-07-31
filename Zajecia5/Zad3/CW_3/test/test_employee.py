import pytest
from personnel.employee import Employee

def test_employee_initialization():
    employee = Employee("Jane", "Smith", 124, 8000.0)
    assert employee.first_name == "Jane"
    assert employee.last_name == "Smith"
    assert employee.employee_id == 124
    assert employee.salary == 8000.0

def test_employee_display_info(capsys):
    employee = Employee("Jane", "Smith", 124, 8000.0)
    employee.display_info()
    captured = capsys.readouterr()
    assert captured.out == "Employee ID: 124, Name: Jane Smith, Salary: 8000.0 zł\n"

def test_employee_update_salary():
    employee = Employee("Jane", "Smith", 124, 8000.0)
    employee.update_salary(9000.0)
    assert employee.salary == 9000.0
