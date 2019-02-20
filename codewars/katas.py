from fractions import Fraction


def mixed_fraction(string):
    """
    Returns a string represenation of a mixed fraction.
    e.g.
    Input: 42/9, expected result: 4 2/3
    """
    frac = Fraction(*map(int, string.split("/")))
    if frac.denominator == 1:
        return f"{frac.numerator}"
    whole = int(
        abs(frac.numerator) / frac.denominator * (1 if frac.numerator > 0 else -1)
    )
    frac = abs(frac - whole) if whole else frac - whole
    return f"{whole} {frac}" if whole else f"{frac}"


def data_reverse(data):
    """
    Reverses the order of 8 bits
    """
    bit_size = 8
    parsed_bits = [data[i : i + bit_size] for i in range(0, len(data), bit_size)]
    rev_list = parsed_bits[::-1]
    flat_list = [item for sublist in rev_list for item in sublist]
    return flat_list


def descending_order(num):
    """
    returns an integer sorted by number
    """
    return int("".join(sorted(str(num), reverse=True)))


def find_next_square(sq):
    """
    Returns the next perfect square if a perfect square is inputted, otherwise -1
    """
    root = sq ** 0.5
    return int(root + 1) ** 2 if root.is_integer() else -1


def nb_year(p0, percent, aug, p):
    """
    p0 = starting population
    percent = percent change 
    aug = inhabitants immigrating or emigrating
    p = population to surpass
    
    -> int number of years until population is surpassed
    """
    years = 0
    while p0 < p:
        p0 += (p0 * percent / 100) + aug
        years += 1
    return years
    # your code


def find_short(string):
    """
    Find the length of the shortest word in a sentence.
    """
    return min([len(x) for x in string.split(" ")])


def open_or_senior(data):
    """
    take a nested list, containing age and handicap. 
    If age >= 55 and hanidcap is > 7, then Senior, otherwise Open
    """
    return [
        "Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data
    ]


def count(string):
    """
    return a dict of the number of letters in a string
    e.g. 'aba' -> { 'a': 2, 'b': 1 }
    """
    return {i: string.count(i) for i in string}


def capitals(word):
    """
    Find index of capital letters in a word
    """
    return [idx for (idx, x) in enumerate(word) if x.isupper()]


from fractions import gcd


def get_lcm(lst):
    return reduce(lambda x, y: x * y / gcd(x, y), lst)


def convertFracts(lst):
    """
    Converts a list of fractions into one with a shared common denominator
    """
    lcm = get_lcm([y for x, y in lst])
    return [[x * lcm / y, lcm] for x, y in lst]


def expanded_form(num):
    """
    Converts a number into expanded form
    e.g. 153 = '100 + 50 + 3'
    """
    num = str(num)
    return " + ".join(
        digit + "0" * (len(num) - idx - 1)
        for idx, digit in enumerate(num)
        if digit != "0"
    )


from operator import mul
from functools import reduce


def persistence(num):
    """
    Multiplies the digits of a number together until it reaches a single digit.
    Returns the number of steps it took to get there.
    """
    steps = 0
    while num >= 10:
        num_list = [int(digit) for digit in str(num)]
        num = reduce(mul, num_list)
        steps += 1
    return steps
