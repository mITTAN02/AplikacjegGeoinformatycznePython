import pytest
from personnel.driver import Driver

def test_driver_initialization():
    driver = Driver("John", "Doe", 123, 5000.0, "DL12345", ["BLS"])
    assert driver.first_name == "John"
    assert driver.last_name == "Doe"
    assert driver.employee_id == 123
    assert driver.salary == 5000.0
    assert driver.license_number == "DL12345"
    assert driver.qualifications == ["BLS"]

def test_driver_display_info():
    driver = Driver("John", "Doe", 123, 5000.0, "DL12345", ["BLS"])
    info = driver.display_info()
    assert info == "Driver ID: 123, Name: John Doe, Salary: 5000.0, License Number: DL12345, Qualifications: BLS"
