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
