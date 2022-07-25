import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('BlockBuster')


def get_user_input():
    """
    
    """
    # while True:
    print("Please choose what you would like to do\n")
    print("1:Check in-store stock\n")
    print("2:Add or remove in-store stock\n")
    print("3:Check In-store stock\n")

    choice_input = input("Please enter the corresponding number.\n")

    choice = int(choice_input)

    print(f"You chose option {choice}")


get_user_input()