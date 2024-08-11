# Function 1: Takes a string and converts it into a base 10 number and returns
# it. Uses helper functions integer_check_and_convert, float_check_and_convert,
#  and hex_check_and_convert
def conv_num(num_str):
    # If input empty or not a string, return None
    if not isinstance(num_str, str) or not num_str:
        return None

    integer_final_result = integer_check_and_convert(num_str)
    # Calls helper function to see if value is a valid integer and does the
    # conversion
    if integer_final_result is not None:
        return integer_final_result

    float_final_result = float_check_and_convert(num_str)
    # Calls helper function to see if value is a valid integer and does the
    # conversion
    if float_final_result is not None:
        return float_final_result

    hex_final_result = hex_check_and_convert(num_str)
    if hex_final_result is not None:
        return hex_final_result

    return None


def integer_check_and_convert(num_str):
    """Helper function to check validity of input and converts string to an
    integer"""
    sign_result = 1    # Default a positive number
    if num_str and num_str[0] == '-':   # If integer is a negative
        sign_result = -1
        num_str = num_str[1:]   # Removes the negative sign

    # Handles case where string is empty if negative sign is removed
    if not num_str:
        return None

    # Converts string values to integers
    character_conversions = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                             '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    num_value = 0
    for character in num_str:
        if character in character_conversions:  # If character is valid
            # Update num_value by multiplying current by 10 and adding the
            # digit
            num_value = num_value * 10 + character_conversions[character]
        else:
            return None

    return sign_result * num_value  # Multiply value by the sign for result


def float_check_and_convert(num_str):
    """Helper function to check the validity of input and convert string to a
    float"""
    if num_str.count('.') != 1:
        return None

    whole_number, value_after_decimal = num_str.split('.')

    # If no whole number or just negative sign, return None
    if whole_number in ('', '-') and not value_after_decimal:
        return None

    number_value = 0 if whole_number in (
        # Uses helper function to convert whole number
        '', '-') else integer_check_and_convert(whole_number)
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

    # Combines both parts of floating point number forfinal results
    if number_value < 0:
        # If negative, subtracts fractional part
        return number_value - (num_after_decimal / fraction_divisor)
    else:
        # If positive, adds fractional part
        return number_value + (num_after_decimal / fraction_divisor)


def hex_check_and_convert(num_str):
    """Helper function to check the validity of input and convert string to
    integer from hexadecimal"""

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
                             'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14,
                             'f': 15}

    number_value = 0
    for character in num_str:
        # If character is valid
        if character.lower() in character_conversions:
            number_value = number_value * 16 + \
                character_conversions[character.lower(
                )]  # Multiply current value by 16 and add converted digit
        else:
            return None

    return sign_result * number_value   # Adds sign to final result


# Function 3
# Uses helper functions helper_dec_to_hex, helper_hex_to_big,
# hex_to_spaced_hex, and reverse_bytes
def conv_endian(num, endian='big'):
    """
    Takes an integer value as num and converts it to a hexadecimal number.
    The endian type is determined by the flag endian.
    The function will return the converted number as a string
    """

    # Edge case if endian is not 'big' or 'little':
    if endian != 'big' and endian != 'little':
        return None

    # Convert integer to a hexadecimal string
    hex_string = helper_dec_to_hex(num)

    # Convert hex string to big endian
    big_endian = helper_hex_to_big(hex_string)

    # Add spaces to each byte
    spaced_hex_string = hex_to_spaced_hex(big_endian)

    # If endian = 'little'
    if endian == 'little':
        spaced_hex_string = reverse_bytes(spaced_hex_string)

    # Case if num is a negative int return negative hex string
    if num < 0:
        return '-' + spaced_hex_string

    return spaced_hex_string


def helper_dec_to_hex(num):
    """
    Takes an integer value as num and converts it to a hexadecimal number
    in the form of a string
    """
    hex_symbols = '0123456789ABCDEF'

    # Edge case if num is zero
    if num == 0:
        return '0'

    # Case if negative number, take absolute value to convert to a
    # positive number
    if num < 0:
        num = abs(num)

    # Resulting hex string
    result_hex_string = ''

    # Manually convert to hexadecimal number
    while num > 0:
        # Take the remainder
        remainder = num % 16
        # Append corresponding hex symbol
        result_hex_string = hex_symbols[remainder] + result_hex_string
        # Floor division and assign number
        num //= 16

    return result_hex_string


def helper_hex_to_big(hex_string):
    """
    Takes hexadecimal string and converts it into Big Endian Ordering
    """
    # Add leading zero if hex string is not even length
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string

    # Split hex string into bytes of two characters
    big_endian = []
    for i in range(0, len(hex_string), 2):
        # Takes a slice of 2 characters and append it to the list
        byte_pair = hex_string[i:i+2]
        big_endian.append(byte_pair)

    return big_endian


def hex_to_spaced_hex(hex_string):
    """
    Takes hexadecimal string and converts it into correct single spaced format
    """
    spaced_hex = ' '.join(hex_string)
    return spaced_hex


def reverse_bytes(hex_string):
    """
    Takes hexadecimal string and reverses it for Little Endian Ordering
    """
    # Split the string into byte groups
    byte_groups = hex_string.split(' ')

    # Reverse the order of byte groups
    reversed_byte_groups = byte_groups[::-1]

    # Join the reversed byte groups with spaces
    reversed_string = ' '.join(reversed_byte_groups)

    return reversed_string
