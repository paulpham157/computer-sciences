# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
# Free under certain conditions — see the license for details.

FILENAME = 'test.dat'


def main():
    with open(FILENAME, "w") as my_file:
        my_file.write("Hello! This is my first file.\n")
        my_file.write("Hello! This is my first file.\n")


if __name__ == '__main__':
    main()
