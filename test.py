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
