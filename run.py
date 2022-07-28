from pprint import pprint  # Used to make some print statements easier to read
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


def get_user_input():
    """
    Main function to get the users input and decide which function
    or process they want to call
    returns choice that the user inputs
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
    validates the data by raising an error
    if the correct input wasn't used in the "get user input()"
    Param:
    takes a data parameter that comes from a variable which
    contains the users input
    returns true if the data is 1,2 or 3 anything else and it returns false
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
    this function opens the google sheet and through panda
     formats the table neatly in the terminal
     then returns the user to the main function
    """
    # the below method of taking the sheet and printing it
    # in a clearer way was used in RickofManc's project
    # I will link to it in the README
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
    this function is very similair to the get user unput()
    it collects the user input and then enters that
    data into the spreadsheet
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
    """
    this function is the same as the add_units()
    it adds the user input to a different sheet
    they both run off of a while loop so
    if the user input is invalid they can retry
    """
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
    this function iterates through the list passed from the add_units()
    and add_rent() functions and converts that lists items into an
    index, it then makes sure that there is exactly 6 items
    in the list, if there is less or more it raises a
    ValueError
    Param:
    the data parameter takes the variables given from both the add_units()
    and add_rent() functions in order to turn them into a list.
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
    this function opens the selected worksheet and
    appends a new row to the bottom of the sheet
    with data given from another function
    param:
    takes a worksheet parameter to decide which worksheet
    to append the data too
    and a data parameter that determines what data should be added
    """
    print(f"Updating {worksheet} sheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} updated successfully...\n")
    # this is a bit counter-intuitive but this for when the total stock
    # is calculated, it prints to the terminal
    if worksheet == "Total":
        total_sheet = pd.DataFrame(SHEET.worksheet("Total").get_all_records())
        print(tabulate(
            total_sheet, headers='keys', tablefmt='pretty', showindex="never"))

    get_user_input()


def total_stock():
    """
    this function calculates the total stock by
    gointo the "Stock" and "Rented" sheets and getting the last row from each
    it then creates an empty list and goes through each item
    from both sheets, adds them together and puts them in the empty list
    which is then updated and sent to the "Total" sheet
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
    main funtion used to start the program
    """
    get_user_input()


main()
