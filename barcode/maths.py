import math
from barcode.config import valid_lengths


def calculate_check_digit(input_digits):

    if not len(str(input_digits)) in valid_lengths:
        raise ValueError("Invalid length for non-check-digits.  Valid lengths are {}".format(valid_lengths))

    s = sum([int(x) * 3 ** (((i % 2) + len(str(input_digits))) % 2) for i, x in enumerate(str(input_digits))])

    #   s: the sum-product of check-digits

    #   >>>        int(x)        *       3 ** (((i % 2) + len(str(input_digits)) - 1) % 2)
    #   the multiplicand sequence repeats, starting at 3 for odd-numbered inputs, 1 for even-numbered
    #   this allows us to make use of the modulo operator (%) of 2 to alternate between 3^1 (=3) and 3^0 (=1)

    #   >>>        for i, x in enumerate(str(input_digits))
    # a list comprehension on enumerate(input-as-string) will give us the index, i, to use here along with each digit
    # with an (iterable) array of products resulting from the list comprehension

    # quick-and-dirty way to work around ceiling() function's integer-scope limitation by shifting the decimal

    return (10 * math.ceil(s/10)) - s