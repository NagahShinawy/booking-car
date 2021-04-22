"""
created by Nagaj at 21/04/2021
"""
import json


def load_cars():
    """

    :return: list of sorted cars by id
    """
    with open("cars.json", "r") as cars_file:
        cars = json.load(cars_file)
    # sort cars by id
    cars = sorted(cars, key=lambda car: car["id"])
    return cars


def get_booking_history():
    """

    :return: all booking were done
    """
    with open("booking.json", "r") as booking_file:
        booking = json.load(booking_file)
    return booking


def save_to_history(history: list, booking: dict):
    """

    :return: save booking to history
    """
    history.append(booking)
    with open("booking.json", "w") as booking_file:
        json.dump(history, booking_file, indent=4)
