"""
This program is for store managers or another user that works in
inventory control, to precisely look at and manage stock for
a BlockBuster chain video rental store.
"""
import sys
import gspread  # Needed to open and edit spreadsheet
import pandas as pd  # Used as a way to make the sheet more comprehensible
from tabulate import tabulate  # Used to help render panda DFs
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
MAX_ALLOWED_STOCK = 200


def get_user_input():
    """
    Main function to get the users input and decide which function
    or process they want to call
    returns choice that the user inputs.
    """
    while True:
        print("\nPlease choose what you would like to do\n")
        print("1:Check in-store and rented stock\n")
        print("2:Add this weeks in-store and rented stock\n")
        print("3:Check total stock\n")
        print("4:Exit\n")

        choice = input("Please enter the corresponding number.\n").strip()

        if validate_input(choice):
            print("\nInput received...\n")
            break

    if choice == "1":
        check_stock()

    elif choice == "2":
        add_units("Stock", "Please enter this week's in-store stock.")
        add_units("Rented", "Please enter this week's rented stock.")

    elif choice == "3":
        total_stock()

    elif choice == "4":
        sys.exit(0)

    get_user_input()


def validate_input(data):
    """
    Validates the data by raising an error
    if the correct input wasn't used in the "get user input()"
    Param:
    takes a data parameter that comes from a variable which
    contains the users input
    returns true if the data is 1,2 or 3 anything else and it returns false.
    """
    if data not in {"1", "2", "3", "4"}:
        print(f"Incorrect option. you selected {data}")
        return False

    return True


def check_stock():
    """
    this function opens the google sheet and through panda
     formats the table neatly in the terminal
     then returns the user to the main function.
    """
    # the below method of taking the sheet and printing it
    # in a clearer way was used in RickofManc's project
    # I will link to it in the README
    print("\n\nGetting in-store stock data...\n")
    stock = pd.DataFrame(SHEET.worksheet("Stock").get_all_records())
    print(tabulate(
        stock, headers='keys', tablefmt='pretty', showindex="never"))

    print("\n\nGetting rented stock data...\n")
    rt = pd.DataFrame(SHEET.worksheet("Rented").get_all_records())
    print(tabulate(
        rt, headers='keys', tablefmt='pretty', showindex="never"))


def add_units(worksheet, message):
    """
    this function is very similair to the get user unput()
    it collects the user input and then enters that
    data into the spreadsheet.
    param:
    this function takes two parameters, the first
    "worksheet tells the function which sheet to draw the data and
    headers from, the second is for the printed messages.
    """
    print(f"\n{message}\n")
    print("\nLast week's stock.\n")
    stock = pd.DataFrame(SHEET.worksheet(worksheet).get_all_records())
    print(tabulate(
        stock, headers='keys', tablefmt='pretty', showindex="never"))

    films = stock.columns

    # List containing this week's stock numbers for each film in order.
    stock_data = []

    for film in films:

        while True:
            user_input = input(
                f"\nPlease enter stock for this week for {film}.\n"
            ).strip()

            try:
                count = int(user_input)
                if count < 0 or count > MAX_ALLOWED_STOCK:
                    raise ValueError("Stock input greater than maximum.")
            except ValueError:
                print(f"Invalid input. Input should be a number between 0 "
                      f"and {MAX_ALLOWED_STOCK}.")
                continue
            stock_data.append(count)
            break

    update_stock_sheet(worksheet, stock_data)


def update_stock_sheet(worksheet, data):
    """
    this function opens the selected worksheet and
    appends a new row to the bottom of the sheet
    with data given from another function.
    param:
    takes a worksheet parameter to decide which worksheet
    to append the data too
    and a data parameter that determines what data should be added.
    """
    print(f"Updating {worksheet} sheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} updated successfully...\n")

    print("\nUpdated Data...\n")
    stock = pd.DataFrame(SHEET.worksheet(worksheet).get_all_records())
    print(tabulate(
        stock, headers='keys', tablefmt='pretty', showindex="never"))


def total_stock():
    """
    this function calculates the total stock by
    gointo the "Stock" and "Rented" sheets and getting the last row from each,
    it then creates an empty list and goes through each item
    from both sheets, adds them together and puts them in the empty list
    which is then updated and sent to the "Total" sheet.
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


def main():
    """
    main funtion used to start the program.
    """
    get_user_input()


main()
