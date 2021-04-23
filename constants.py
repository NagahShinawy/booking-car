"""
created by Nagaj at 22/04/2021
"""
# ################  cars messages  #########################
CAR_DETAILS = "{car_id}-{car_model}-{car_color}"
BOOKED_CAR = "Your Booked <{booked_car}>"
VALID_CARS_IDS = "Enter Valid Car Id from List {}"
CANCEL_BOOKING = "You Canceled The Booking For Car <{}>"
NO_BOOKING_TO_RETRIEVE = "You Have Not Booked Car To Retrieve It"
NO_BOOKING_TO_CANCEL = "You Have Not Booked Car To Cancel"
NO_CAR_TO_SHOW = "No Cars To Show, You Can Book Now"
BACK_CAR = "The Car <{}> Get Back To Store Again"
YOUR_CAR = "Your Car is <{}>"
# ####################  commands ######################################


ACCEPT = "y"
CLOSE = "x"
LIST = "l"
BOOK = "b"
CANCEL = "c"
RETRIEVE = "r"
SHOW = "s"

ACTION_OPTIONS = ("l", "s", "b", "c", "r", "x")
ACCEPT_REFUSE_OPTIONS = ("y", "n")

# ############### shell message #########################

OPENING_MSG = (
    "Enter Your Command l[List], s[Show],  b[Book] c[Cancel], r[Retrieve] x[close]"
)

INVALID__OPTION_COMMAND = "Invalid <{command}> Enter Your Command l[list], b[Book] c[Cancel], r[Retrieve] x[close]"
INVALID_ACCEPT_REFUSE_COMMAND = "Invalid <{command}> Enter Your Command y[yes], n[no]"
RATE_US_MSG = "Do You Want To Rate Us ? y[yes], n[no]"
RATE_TEXT = "Enter Your Rating Text"
THANKS = "Thanks For Rating"
BYE = "Done. Goodbye"

# #################  Error Messages  ####################

SHORT_TEXT = 'Short Text <{}>, Min Text Length Is 3'
ALL_CHARS_ARE_NUMBERS = "All Of Your Text <{}> Are Numbers!. Please Type Valid Text"

# ########################  Datetime Format  ########################

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
