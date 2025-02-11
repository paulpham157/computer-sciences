# Copyright © 2020 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
# Free under certain conditions — see the license for details.

NUM_VALUES = 60000

from random import randint


def main():
    """Main entry point"""

    die_values = list()
    for i in range(NUM_VALUES):
        die_values.append(randint(1, 6))
    for i in range(NUM_VALUES // 10):
        die_values.append(6)

    if check(die_values):
        print("Whoa, dice is fair")
    else:
        print("Watchout!!!! Dice is *NOT* fair")


def check(values):
    """Check whether the dice is fair"""

    # step 1: count results
    frequency = list()
    for r in range(6):
        frequency.append(values.count(r + 1) / len(values))
    print(frequency)

    # check them
    expected_frequency = 1 / 6
    acceptable_error = 0.01
    all_correct = True
    for f in frequency:
        if abs(f - expected_frequency) > acceptable_error:
            all_correct = False

    return all_correct


if __name__ == '__main__':
    main()
