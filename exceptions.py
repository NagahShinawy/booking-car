"""
created by Nagaj at 22/04/2021
"""
from constants import SHORT_TEXT, ALL_CHARS_ARE_NUMBERS


class ShortLenError(Exception):
    message = SHORT_TEXT


class TextAsNumber(Exception):
    message = ALL_CHARS_ARE_NUMBERS
