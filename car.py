"""
created by Nagaj at 21/04/2021
"""
import json


def load_cars():
    with open("cars.json", "r") as f:
        cars = json.load(f)
    # sort cars by id
    cars = sorted(cars, key=lambda car: car["id"])
    return cars


def booking_history():
    with open("booking.json", "r") as f:
        booking = json.load(f)
    return booking
