# Copyright © 2020 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
# Free under certain conditions — see the license for details.

import random


def main():
    """Main entry point"""

    array = []
    for i in range(10000):
        array.append(random.randint(-1_000_000_000, +1_000_000_000))
    print(array)

    smallest = largest = array[0]
    for e in array:
        if e > largest:
            largest = e
        if e < smallest:
            smallest = e
    print(f"Largest: {largest}, smallest: {smallest}")

    smallest = largest = None
    for e in array:
        if largest is None or e > largest:  # ie. largest == None
            largest = e
        if smallest is None or e < smallest:
            smallest = e
    print(f"Largest: {largest}, smallest: {smallest}")


if __name__ == '__main__':  # BLACK MAGIC!
    main()
