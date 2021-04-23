"""
created by Nagaj at 22/04/2021
"""
import datetime
import json

from constants import THANKS, DATETIME_FORMAT
from exceptions import ShortLenError, TextAsNumber


def load_rates():
    with open("rates.json", "r") as rates_file:
        rates = json.load(rates_file)
    return rates


class RateUs:
    MIN_TEXT_LEN = 3
    rates: list = load_rates()

    def __init__(self, text: str):
        self.text = self.set_text(text)
        self.timestamp = datetime.datetime.strftime(
            datetime.datetime.now(), DATETIME_FORMAT
        )

    def __str__(self):
        return self.text

    def set_text(self, text: str):
        if len(text) < self.MIN_TEXT_LEN:
            raise ShortLenError(ShortLenError.message.format(text))
        if text.isdecimal():
            raise TextAsNumber(TextAsNumber.message.format(text))
        return text

    def save(self):
        single_rate = {
            "text": self.text,
            "datetime": datetime.datetime.strftime(
                datetime.datetime.now(), DATETIME_FORMAT
            ),

        }
        self.rates.append(single_rate)
        with open("rates.json", "w") as rate_file:
            json.dump(self.rates, rate_file, indent=4)
        print(THANKS)
