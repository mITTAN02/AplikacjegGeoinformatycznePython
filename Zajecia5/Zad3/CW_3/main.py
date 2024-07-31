from fleet.ambulance import Ambulance
from fleet.station import Station
from operations import *
from personnel import *
import random
from log import configure_logging
import logging
import argparse

def run_application():
    configure_logging()
    logging.info("Starting the application")

    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance("Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])

    employee1 = Employee("John", "Doe", 123, 12000.0)
    employee2 = Employee("Jane", "Smith", 124, 8000.0)

    driver1 = Driver("Mike", "Johnson", 125, 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 126, 11500.0, "DL12346", ["ALS", "PHTLS"])

    if ambulance1 == ambulance2:
        logging.error("To są te same karetki!")
        raise ValueError("To są te same karetki!")
    
    logging.info(f"Number of working ambulances: {Ambulance.get_instances_count()}")

    queue = IncidentQueue()

    prio1 = random.randint(1,100)
    incident1 = Incident("Power outage in sector 4", (53,25), prio1, "06:00")
    prio2 = random.randint(1,100)
    incident2 = Incident("Fire alarm in building 21", (51,21), prio2, "15:00")

    queue += incident1
    queue += incident2

    logging.info("Aktualne zgłoszenia:")
    logging.info(queue)

    station1 = Station((51, 20), ambulance1, driver1.display_info(), employee1.display_info())
    logging.info(f'Station one: {station1}')
    station2 = Station((51, 20), ambulance2, driver2.display_info(), employee2.display_info())
    logging.info(f'Station one: {station2}')

    logging.info(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    logging.info(f"Po podwyżce: {driver1.display_info()}")

    incident1.add_ambulance(ambulance1)
    incident2.add_ambulance(ambulance2)

    ambulance1.ambulance_done()
    ambulance2.ambulance_done()

def create_parser():
    parser = argparse.ArgumentParser(description='Zarządzanie flotą karetek')
    parser.add_argument('--ambulances', type=int, required=True, help='Liczba dostępnych karetek')
    parser.add_argument('--employees', type=int, required=True, help='Liczba dostępnych pracowników')
    return parser

def run_application(args):
    configure_logging()
    logging.info("Starting the application with CLI arguments")

    num_ambulances = args.ambulances
    num_employees = args.employees

    logging.info(f"Number of ambulances: {num_ambulances}")
    logging.info(f"Number of employees: {num_employees}")


    ambulances = [Ambulance(f"Type {i}", "available", (50.0, 19.0), ["Equipment"]) for i in range(num_ambulances)]
    employees = [Employee(f"First{i}", f"Last{i}", i, 5000.0) for i in range(num_employees)]

 

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    run_application(args)