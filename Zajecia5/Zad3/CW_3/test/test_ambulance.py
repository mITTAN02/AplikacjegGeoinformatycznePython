import pytest
from fleet.ambulance import Ambulance
from operations.incident import Incident

def test_ambulance_initialization():
    ambulance = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    assert ambulance.vehicle_type == "Type A"
    assert ambulance.status == "available"
    assert ambulance.location == (50.095340, 18.920282)
    assert ambulance.medical_equipment == ["Defibrillator", "Oxygen tank"]
    assert ambulance.state == 'coffee break'

def test_ambulance_update_location():
    ambulance = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    new_location = (50.110340, 19.920282)
    ambulance.update_location(new_location)
    assert ambulance.location == new_location
    assert ambulance.state == 'hitting the road'

def test_ambulance_add_incident():
    ambulance = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    incident = Incident("Test incident", (52, 21), 50, "12:00")
    ambulance.add_incident(incident)
    assert ambulance.incident[0] == incident
    assert ambulance.state == 'got incident'

def test_ambulance_sort_incident():
    ambulance = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    incident1 = Incident("Test incident 1", (52, 21), 30, "12:00")
    incident2 = Incident("Test incident 2", (53, 22), 20, "11:00")
    ambulance.add_incident(incident1)
    ambulance.add_incident(incident2)
    ambulance.sort_incident()
    assert ambulance.incident[0] == incident2
    assert ambulance.incident[1] == incident1

def test_ambulance_equality():
    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    assert ambulance1 != ambulance2

def test_ambulance_str():
    ambulance = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    assert str(ambulance) == "Ambulance ID: 1, Type: Type A, Status: available, Location: (50.09534, 18.920282), Equipment: Defibrillator, Oxygen tank"
