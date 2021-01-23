"""Convert numbers in words (string) to int() numbers"""

def million_sep(string):
    """func to separate number words in million section"""
    x = 0
    num_m = 0      #save index of a 'million'

    for el in string:
        if el == 'million':
            num_m = string.index(el)

    new_string = string[num_m + 1:]
    million_list = []
    while x < num_m:
        million_list.append(string[x])
        x += 1
    return new_string, million_list


def thousand_sep(string):
    """func to separate number words in thousand section"""
    x = 0
    num_t = 0               #save index of 'thousand'

    for el in string:
        if el == 'thousand':
            num_t = string.index(el)

    new_string = string[num_t + 1:]
    thousand_list = []

    while x < num_t:
        thousand_list.append(string[x])
        x += 1

    return new_string, thousand_list


def counter(string, sep):      #sep : the number that numebr should multiple to .(EX : if program is chekcing the million section numbers , result number should multiple to 1000000)
    """func to translate words to numbers"""
    res = 0
    all_dic = {"a_hundred": 100, "one_hundred": 100, "two_hundred": 200, "three_hundred": 300, "four_hundred": 400,
               "five_hundred": 500, "six_hundred": 600, "seven_hundred": 700, "eight_hundred": 800,
               "nine_hundred": 900,
               "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80,
               "ninety": 90,
               "ten": 10, "zero": 0, "a": 1, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
               "eight": 8,
               "nine": 9,
               "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
               "seventeen": 17, "eighteen": 18, "nineteen": 19}
    string_list = string.split()
    for el in string_list:
        res += all_dic[el] * sep

    return res


def parse_int(string: str):
    string = string.lower().replace('-', ' ').replace(' and', ' ').replace('  ', ' ').replace(' hundred', '_hundred').split(' ')
    string.append('zero')
    res = 0

    s = ' '
    if 'million' in string:
        string, million = million_sep(string)
        million_str = s.join(million)
        res += counter(million_str, 1_000_000)

    if 'thousand' in string:
        string, thousand = thousand_sep(string)
        thousand_str = s.join(thousand)
        res += counter(thousand_str, 1000)

    hundred_str = s.join(string)
    res += counter(hundred_str, 1)
    return res
