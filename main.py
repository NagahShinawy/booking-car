"""
created by Nagaj at 21/04/2021
"""
from user import User

if __name__ == "__main__":
    john = User()
    john.list_cars()
    john.book_car(5)
    john.retrieve_car()
    john.cancel_booking()
