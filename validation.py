"""
created by Nagaj at 22/04/2021
"""


def validate_car_id(cars_ids, car_id):
    while car_id not in cars_ids:
        try:
            car_id = int(input("Enter TESTING Valid Car Id from List {}".format(cars_ids)))
        except ValueError:
            continue
    return car_id
