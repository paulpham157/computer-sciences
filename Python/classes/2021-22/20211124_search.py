# Copyright © 2021 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
# Free under certain conditions — see the license for details.

import random

LIST_LENGTH = 100
MIN_VALUE = 0
MAX_VALUE = 999


def main():
    my_list = list()
    for n in range(LIST_LENGTH):
        my_list.append(random.randint(MIN_VALUE, MAX_VALUE))

    value = int(input())
    pos = None
    for i, v in enumerate(my_list):
        if pos is None and v > value:
            pos = i

    if pos is not None:
        print(f"The first value >{value} is {my_list[pos]} at position {pos}")
    else:
        print(f"There are no values >{value}!")


main()
