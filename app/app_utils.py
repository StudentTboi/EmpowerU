"""
FIT1056 2024 Semester 2
Programming Concepts Task 5
This file contains the definitions for common utility functions.
"""

def read_file(filepath):
    """
    This function reads a file at the specified path and returns the 
    text stored. UTF-8 encoding is expected.
    (More about UTF-8: https://en.wikipedia.org/wiki/UTF-8)

    Parameters:
    - filepath: str, path of the file to be read
    
    Returns:
    if file could be successfully read, a list of strings containing each line in the file,
    None otherwise.
    """
    successful_read = False
    try:
        with open(file=filepath, mode="r", encoding="utf8") as f:
            lines = f.readlines()
        if len(lines) == 0:
            print("WARNING: File is empty.")
        successful_read = True
    except FileNotFoundError:
        print("ERROR: File not found.")
    except UnicodeDecodeError:
        print("ERROR: Could not decode file with UTF-8 encoding.")
    finally:
        if successful_read:
            return lines

def append_to_file(filepath, contents):
    """
    This function appends the contents to a file at the specified path.
    UTF-8 encoding is expected.
    (More about UTF-8: https://en.wikipedia.org/wiki/UTF-8)

    Parameters:
    - filepath: str, path of the file to have contents appended
    - contents: str, to be appended to the file

    Returns:
    - bool: True if it is successfully appended, False otherwise
    """
    successful_append = False
    try:
        with open(file=filepath, mode="a", encoding="utf8") as f:
            f.write(contents)
        successful_append = True
    except FileNotFoundError:
        print("ERROR: File not found.")
    except UnicodeDecodeError:
        print("ERROR: Could not decode file with UTF-8 encoding.")
    finally:
        return successful_append

def is_valid_first_name(input_first_name):
    if len(input_first_name) > 0:
        return True
    else:
        return False

def is_valid_time_format(input_time_value):
    """
    This function checks whether the string value input by the user is
    a valid time *AND* presented in HH:mm format

    Parameters:
    - input_time_value: str, the value provided by the user

    Returns:
    bool - True if input value is a valid time in HH:mm format, 
           False otherwise
    """
    if len(input_time_value) == 5 and input_time_value[2] == ":":
        hour, minute = input_time_value.split(":")
        if hour.isdigit() and minute.isdigit():
            hour = int(hour)
            minute = int(minute)
            return hour in range(24) and minute in range(60)

    return False    

def is_valid_contact_number(input_contact_number):
    all_valid_digits = True
    for char in input_contact_number:
        if char not in "0123456789":
            all_valid_digits = False
            break
    if len(input_contact_number) == 10 and all_valid_digits:
        return True
    return False


def is_valid_date_format(input_date_value):
    """
    This function checks whether the string value input by the user is 
    a valid date (on or after 1800, and on or before 2024) *AND* presented in DD/MM/YYYY format

    Parameters:
    - input_date_value: str; the value provided by the user

    Returns:
    bool - True if input value is a valid date in DD/MM/YYYY format (on or before 2024), 
           False otherwise
    """

    numeric_chars = "0123456789"

    if len(input_date_value) == 10 and input_date_value[2] == "/" and input_date_value[5] == "/":
        day, month, year = input_date_value.split("/")

        if (all([char in numeric_chars for char in day]) 
            and all([char in numeric_chars for char in month]) 
            and all([char in numeric_chars for char in year])):

            day = int(day)
            month = int(month)
            year = int(year)
            return is_date_valid(day, month, year)

    return False

def is_date_valid(day, month, year):
    """
    This function checks whether the given date exists in the Gregorian calendar.

    Parameters:
    - day: int, (converted) integer value of the day
    - month: int, (converted) integer value of the month
    - year: int, (converted) integer value of the year in the Gregorian calendar

    Returns:
    bool - True if the given date exists in the Gregorian calendar, False otherwise
    """
    valid_days = None
    valid_months = range(1, 13)

    if month in [1, 3, 5, 7, 8, 10, 12]:
        valid_days = range(1, 32)
    elif month in [4, 6, 9, 11]:
        valid_days = range(1, 31)
    elif month == 2 and is_leap_year(year):
        valid_days = range(1, 30)
    elif month == 2 and not is_leap_year(year):
        valid_days = range(1, 29)
    else:
        return False

    return day in valid_days and month in valid_months and 1800 <= year <= 2024


def is_leap_year(year):
    """
    This function checks if the year is a leap year.

    Parameters:
    - year: int

    Returns:
    bool - True if given year is a leap year, False otherwise
    """
    # Utilising Python smart evaluation
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# DO NOT MODIFY BEYOND THIS LINE
if __name__ == "__main__":
    read_file("./pst5_app.py")