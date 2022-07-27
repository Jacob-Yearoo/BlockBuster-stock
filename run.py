import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    while True:
        print("Please choose what you would like to do\n")
        print("1:Check in-store stock\n")
        print("2:Add this weeks in-store stock\n")
        print("3:Check total stock\n")

        choice_input = input("Please enter the corresponding number.\n")

        choice = choice_input
        validate_input(choice)

        if validate_input(choice):
            print("Input received...\n")
            break
        
    if choice == "1":
        check_stock()
    
    # if choice == "2":
    #     check_stock()
    
    # if choice == "3":
    #     check_stock()

    return choice


def validate_input(data):
    """
    
    """
    try:
        int(data)
        while data not in ["1", "2", "3"]:
            raise ValueError(
                f"Incorrect option. you selected {data}"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False

    return True


def check_stock():
    """
    
    """
    print("Getting in-store stock data...\n")
    stock = SHEET.worksheet("Stock").get_all_values()
    pprint(stock)

    get_user_input()


def add_units():
    """
    
    """
    while True:
        print("please enter stock for this weeks blockbusters")
        print("Data should be six numbers")
        print("Example: 10,20,30,40,50,60\n")

        new_str = input("Enter your data here:\n")

        stock_data = new_str.split(",")
        validate_stock(stock_data)

        if validate_stock(stock_data):
            print("Data is valid!")
            break


def validate_stock(data):
    """
    
    """
    try:
        [int(data) for ind in data]
        if len(data) != 6:
            raise ValueError(
                f"Whoops looks like you missed some. you provided {len(data)}"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False

    return True