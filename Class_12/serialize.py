# Write a generator that produces “serial numbers” according to the following rule: a serial number is a
# ten-character string where
# • the first two characters are upper-case alphabetic and
# • the following eight are numeric.
# The alphabetic portion will be all strings from AA through ZZ in lexicographic order (AA,AB,AC
# …). For each alphabetic prefix, the numeric part will be all strings 00000000 – 99999999. So we
# have AA00000000, AA00000001 …ZZ99999999.


def number_serial():
    number = 00000000
    while number < 99999999:
        yield f"{number:08}"
        number += 1


def alphabet_serial():
    right_string = ord("A")  # 65
    left_string = ord("A")
    while right_string and left_string <= 90:
        yield f"{chr(left_string)}{chr(right_string)}"
        right_string += 1
        if right_string > 90:
            right_string = ord("A")
            left_string += 1


a_generator = alphabet_serial()
n_generator = number_serial()
for i in a_generator:
    for j in n_generator:
        print(f"{i}{j}")
