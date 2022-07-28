import gspread
import pandas as pd
from tabulate import tabulate
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
        print("1:Check in-store and rented stock\n")
        print("2:Add this weeks in-store and rented stock\n")
        print("3:Check total stock\n")

        choice_input = input("Please enter the corresponding number.\n")

        choice = choice_input
        validate_input(choice)

        if validate_input(choice):
            print("Input received...\n")
            break
        
    if choice == "1":
        check_stock()
    
    if choice == "2":
        add_units()
    
    if choice == "3":
        total_stock()

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
    stock = pd.DataFrame(SHEET.worksheet("Stock").get_all_records())
    print(tabulate(
        stock, headers='keys', tablefmt='pretty', showindex="never"))

    print("Getting rented stock data...\n")
    rt = pd.DataFrame(SHEET.worksheet("Rented").get_all_records())
    print(tabulate(
        rt, headers='keys', tablefmt='pretty', showindex="never"))

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
    pprint(f"You inputted {stock_data}")
    update_stock_sheet("Stock", stock_data)

    add_rent()


def add_rent():
    while True:
        print("Now enter the units that are currently rented out")
        print("Data should be six numbers")
        print("Example: 10,20,30,40,50,60\n")

        rent_str = input("Enter your data here:\n")

        rent_data = rent_str.split(",")
        validate_stock(rent_data)

        if validate_stock(rent_data):
            print("Data is valid!")
            break
    pprint(f"You inputted {rent_data}")
    update_stock_sheet("Rented", rent_data)

    get_user_input()


def validate_stock(data):
    """
    
    """
    try:
        [int(x) for x in data]
        if len(data) != 6:
            raise ValueError(
                f"Whoops looks like you missed some. you provided {len(data)}"
            )
    except ValueError as e:
        print(f"Invalid input: {e}, please try again.\n")
        return False

    return True


def update_stock_sheet(worksheet, data):
    """
    
    """
    print(f"Updating {worksheet} sheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} updated successfully...\n")

    if worksheet == "Total":
        total_sheet = pd.DataFrame(SHEET.worksheet("Total").get_all_records())
        print(tabulate(
            total_sheet, headers='keys', tablefmt='pretty', showindex="never"))

    # get_user_input()


def total_stock():
    """
    
    """
    print("Working out totals...\n")
    stock = SHEET.worksheet("Stock").get_all_values()[-1]
    rent = SHEET.worksheet("Rented").get_all_values()[-1]

    total_data = []
    for stock, rent in zip(stock, rent):
        totals = int(stock) + int(rent)
        total_data.append(totals)
        
    update_stock_sheet("Total", total_data)

    return total_data


get_user_input()

