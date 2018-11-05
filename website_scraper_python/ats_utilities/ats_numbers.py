import math


def get_digit_count(number):
    """

    https://stackoverflow.com/questions/2189800/length-of-an-integer-in-python
    # Using log10 is a mathematician's solution
    # Using len(str()) is a programmer's solution
    # The mathematician's solution is O(1) [NOTE: Actually not O(1)?]
    # The programmer's solution in O(log10 n)
    # In fact, log10 probably performs in slower than O(log n)
    # for a faster O(log n) mathematical solution,
    #  first approximate with b = int(n.bit_length() * math.log10(2)),
    #  then round up if necessary by checking if n == 0 or abs(n) >= 10**b
    # My bad: technically floating-point math is greater than O(log n)
    # ...n.bit_length() * math.log10(2) is only very marginally faster than math.log10(n)
    # ...requires exponentiation for its check, (10**b), which takes up most of the time
    # math.log10(n) requires the same check at around 999999999999999
    # Under 10**12, len(str(n)) is the fastest
    # Above 10**12, log10 is the fastest, but above 10**15, it is incorrect
    # Around 10**100 (~log10 with the 10**b check) begins to beat out len(str(n))
    :rtype: boolean
    :param number: number
    :return: digit_count
    """
    # Shall we count the negative sign on negative numbers?
    # Shall we count the decimal place symbol on decimals/floats?
    # Easy, sad option: convert the number to a string and count the characters
    # len(str(123))
    # len(str(abs(v)))
    # # try:
    # #     number = float(number)
    # # except ValueError:
    # #     return None
    # if number > 0:
    #     digit_count = int(math.log10(number)) + 1
    # elif number == 0:
    #     digit_count = 1
    # elif number < 0:
    #     digit_count = int(math.log10(-number)) + 2  # +1 if you do not want to count the '-'
    # else:
    #     digit_count = None
    digit_count = len(str(number))

    return digit_count


def get_number_from_string(string):
    # TODO(JamesBalcomb): make this throw a value error?

    number = None

    if is_integer_number(string):
        number = int(string)
    elif is_floating_number(string):
        number = float(string)

    return number


# def is_integer_number(number):
#
#     try:
#         int(number)
#         return True
#
#     except ValueError:
#         return False


def is_integer_number(number):
    """
    is_integer_number
    :rtype: boolean
    :param number:
    :return:
    """
    is_integer = False
    # Check for a number
    if is_floating_number(number):
        # Check for no remainder, after division by one
        if float(number) % 1 == 0:
            # Check for no decimal point (e.g., 0.0, 1.00000, etc.
            if str(number).find(".") == -1:
                is_integer = True
    return is_integer


def is_floating_number(number):
    """
    is_floating_number
    :param number:
    :return:
    :rtype: boolean
    """
    is_float = False
    try:
        float(number)
        is_float = True
    # except TypeError:
    # return False
    except ValueError:
        is_float = False
    return is_float


def is_unsigned_number(number):
    """
    is_unsigned_number
    :rtype: boolean
    :param number:
    :return:
    """
    is_unsigned = False
    try:
        number = float(number)
    except ValueError:
        is_unsigned = False
    if number >= 0:
        is_unsigned = True
    else:
        is_unsigned = False
    return is_unsigned
