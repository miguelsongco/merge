# Function 2

def my_datetime(num_sec):
    """Convert seconds since epoch to a date in MM-DD-YYYY format."""
    # Convert seconds to minute/hour and hours to days, then seconds to days
    seconds_per_minute = 60
    minutes_per_hour = 60
    hours_per_day = 24
    seconds_per_day = seconds_per_minute * minutes_per_hour * hours_per_day

    # Calculate total days since epoch
    total_days = num_sec // seconds_per_day

    # Get the year and remaining days
    year, remaining_days = get_year_and_remaining_days(total_days)

    # Get the month and day
    month, day = get_month_and_day(year, remaining_days)

    # Format the date as MM-DD-YYYY
    date_string = f"{month + 1:02}-{day:02}-{year}"

    return date_string


def is_leap_year(year):
    """Helper function to check if a given year is a leap year to ensure correct date."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


def get_days_in_month(year, month):
    """Helper function to return the number of days in a given month for a specific year."""
    # set days within each month for non-leap year
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # check Feburary in a leap year
    if month == 1:  # February is index 1
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return days_in_months[month]


def get_year_and_remaining_days(total_days):
    """Helper function to calculate the year from the total number of days since the epoch and return the remaining days."""
    year = 1970

    # loop calculate the year while subtracting days
    while True:
        if is_leap_year(year):
            days_in_current_year = 366
        else:
            days_in_current_year = 365

        if days_in_current_year <= total_days:
            total_days -= days_in_current_year
            year += 1
        else:
            break

    return year, total_days


def get_month_and_day(year, total_days):
    """Helper function to calculate the month and day from the remaining days within a year."""
    month = 0

    # Loop to calculate the month and subtract days
    while True:
        days_in_current_month = get_days_in_month(year, month)

        if days_in_current_month <= total_days:
            total_days -= days_in_current_month
            month += 1
        else:
            break

    day = total_days + 1
    return month, day
=======
# Function 1: Takes a string and converts it into a base 10 number and returns it.
# Uses helper functions integer_check_and_convert, float_check_and_convert, and hex_check_and_convert
def conv_num(num_str):
    # If input empty or not a string, return None
    if not isinstance(num_str, str) or not num_str:
        return None

    integer_final_result = integer_check_and_convert(num_str)
    # Calls helper function to see if value is a valid integer and does the conversion
    if integer_final_result is not None:
        return integer_final_result

    float_final_result = float_check_and_convert(num_str)
    # Calls helper function to see if value is a valid integer and does the conversion
    if float_final_result is not None:
        return float_final_result

    hex_final_result = hex_check_and_convert(num_str)
    if hex_final_result is not None:
        return hex_final_result

    return None


def integer_check_and_convert(num_str):
    """Helper function to check validity of input and converts string to an integer"""
    sign_result = 1    # Default a positive number
    if num_str and num_str[0] == '-':   # If integer is a negative
        sign_result = -1
        num_str = num_str[1:]   # Removes the negative sign

    if not num_str:   # Handles case where string is empty if negative sign is removed
        return None

    # Converts string values to integers
    character_conversions = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                             '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    num_value = 0
    for character in num_str:
        if character in character_conversions:  # If character is valid
            # Update num_value by multiplying current by 10 and adding the digit
            num_value = num_value * 10 + character_conversions[character]
        else:
            return None

    return sign_result * num_value  # Multiply value by the sign for result


def float_check_and_convert(num_str):
    """Helper function to check the validity of input and convert string to a float"""
    if num_str.count('.') != 1:
        return None

    whole_number, value_after_decimal = num_str.split('.')

    # If no whole number or just negative sign, return None
    if whole_number in ('', '-') and not value_after_decimal:
        return None

    number_value = 0 if whole_number in (
        '', '-') else integer_check_and_convert(whole_number)  # Uses helper function to convert whole number
    if number_value is None:
        return None

    num_after_decimal = 0
    fraction_divisor = 1
    # Converts string values to integers
    character_conversions = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                             '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    for character in value_after_decimal:
        if character in character_conversions:
            num_after_decimal = num_after_decimal * \
                10 + character_conversions[character]
            fraction_divisor *= 10   # Multiply divisor by 10 to update
        else:
            return None

    if number_value < 0:  # Combines both parts of floating point number for final results
        # If negative, subtracts fractional part
        return number_value - (num_after_decimal / fraction_divisor)
    else:
        # If positive, adds fractional part
        return number_value + (num_after_decimal / fraction_divisor)


def hex_check_and_convert(num_str):
    """Helper function to check the validity of input and convert string to integer from hexadecimal"""

    # Validate hexadecimal prefix
    if len(num_str) < 2:
        return None
    if num_str[0] == '-':
        # if len is too short or does not have valid prefix, return None
        if len(num_str) < 3 or num_str[1:3].lower() != '0x':
            return None
    else:
        if num_str[:2].lower() != '0x':
            return None
    # Determines if negative or positive
    sign_result = 1
    if num_str[0] == '-':
        sign_result = -1
        num_str = num_str[3:]  # Removes a prefix that is negative hex
    else:
        num_str = num_str[2:]  # Removes positive prefix

    if not num_str:   # If value is empty after removing prefixes, return None
        return None

    # Converts hexadecimal strings to valid integers
    character_conversions = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                             '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                             'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

    number_value = 0
    for character in num_str:
        if character.lower() in character_conversions:   # If character is valid
            number_value = number_value * 16 + \
                character_conversions[character.lower(
                )]  # Multiply current value by 16 and add converted digit
        else:
            return None

    return sign_result * number_value   # Adds sign to final result

