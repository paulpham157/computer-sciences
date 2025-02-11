# Copyright © 2020 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
# Free under certain conditions — see the license for details.

from random import randint


def foo(x):
    if x == 42:
        raise ValueError("Can't handle 42!")
    print(f"x is {x}")


def main():
    try:
        for i in range(100):
            foo(randint(0, 100))
    except ValueError as ve:
        print(f"Yeuch: {ve}")
    finally:
        print("That's all...")


if __name__ == '__main__':
    main()
