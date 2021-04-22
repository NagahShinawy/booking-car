"""
created by Nagaj at 21/04/2021
"""

import datetime

from car import load_cars, save_to_history, get_booking_history
from constant import (
    CAR_DETAILS,
    BOOKED_CAR,
    CANCEL_BOOKING,
    NO_BOOKING_TO_RETRIEVE,
    NO_BOOKING_TO_CANCEL,
    BACK_CAR,
)


class User:
    """
    handles user actions
    """
    cars: list = load_cars()
    history = get_booking_history()

    def __init__(self):
        self.booked_car = None

    def list_cars(self):
        """

        :return: show all cars to user
        """
        for car in self.cars:
            print(
                CAR_DETAILS.format(
                    car_id=car["id"], car_model=car["model"], car_color=car["color"]
                )
            )

    def book_car(self, car_id):
        """

        :param car_id: car id to book it
        :return:
        """
        self.booked_car = self.__find_car_by_id(car_id)
        print(BOOKED_CAR.format(booked_car=self.booked_car))
        self.cars.remove(self.booked_car)

    def cancel_booking(self):
        """
        cancel booking
        :return:
        """
        if self.booked_car is not None:
            self.cars.append(self.booked_car)
            print(CANCEL_BOOKING.format(self.booked_car))
        else:
            print(NO_BOOKING_TO_CANCEL)

    def retrieve_car(self):
        """

        :return: retrieve the car after use it
        """
        if self.booked_car is not None:

            self.cars.append(self.booked_car)
            print(BACK_CAR.format(self.booked_car))
            save_to_history(history=self.history, booking={"car": self.booked_car,
                                                           "datetime": datetime.datetime.strftime(
                                                               datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")})
            self.booked_car = None
        else:
            print(NO_BOOKING_TO_RETRIEVE)

    def rate_service(self):
        """
        :return:
        """

    def __find_car_by_id(self, car_id):
        """

        :param car_id: use car id to get car
        :return: car
        """
        for car in self.cars:
            if car["id"] == car_id:
                return car
