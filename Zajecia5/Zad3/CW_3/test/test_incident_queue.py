import pytest
from operations.incident import Incident
from operations.incident_queue import IncidentQueue

def test_add_incident_to_queue():
    queue = IncidentQueue()
    incident = Incident("Power outage in sector 4", (53, 25), 90, "06:00")
    queue += incident
    assert len(queue) == 1
    assert queue.incidents[0] == incident

def test_queue_ordering():
    queue = IncidentQueue()
    incident1 = Incident("Incident 1", (50, 19), 30, "08:00")
    incident2 = Incident("Incident 2", (51, 20), 20, "09:00")
    incident3 = Incident("Incident 3", (52, 21), 10, "10:00")
    queue += incident1
    queue += incident2
    queue += incident3
    queue.sort()
    assert queue.incidents[0] == incident3
    assert queue.incidents[1] == incident2
    assert queue.incidents[2] == incident1

def test_queue_str():
    queue = IncidentQueue()
    incident = Incident("Power outage in sector 4", (53, 25), 90, "06:00")
    queue += incident
    assert str(queue) == "Incident 0: Power outage in sector 4, location: (53, 25), priority: 90, hour: 06:00, status: Dead or not? We don't know yet\n"
