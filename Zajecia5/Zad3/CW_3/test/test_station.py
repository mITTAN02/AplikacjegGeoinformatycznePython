import pytest
from fleet.ambulance import Ambulance
from fleet.station import Station
from personnel.driver import Driver
from personnel.employee import Employee

def test_station_initialization():
    ambulance = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    driver = Driver("John", "Doe", 123, 5000, "DL123", ["BLS"])
    employee = Employee("Jane", "Doe", 124, 4500)
    station = Station((50.095340, 18.920282), ambulance, driver.display_info(), employee.display_info())
    assert station.location == (50.095340, 18.920282)
    assert station.ambulance == ambulance
    assert station.driver == driver.display_info()
    assert station.employee == employee.display_info()

def test_station_str():
    ambulance = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    driver = Driver("John", "Doe", 123, 5000, "DL123", ["BLS"])
    employee = Employee("Jane", "Doe", 124, 4500)
    station = Station((50.095340, 18.920282), ambulance, driver.display_info(), employee.display_info())
    assert str(station) == f"Station 0: location: (50.09534, 18.920282), ambulance: {ambulance}, driver: {driver.display_info()}, employee: {employee.display_info()}"

def test_station_check_location():
    ambulance = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    driver = Driver("John", "Doe", 123, 5000, "DL123", ["BLS"])
    employee = Employee("Jane", "Doe", 124, 4500)
    station = Station((50.095340, 18.920282), ambulance, driver.display_info(), employee.display_info())
    assert station.location == ambulance.location
    station.check_location()
