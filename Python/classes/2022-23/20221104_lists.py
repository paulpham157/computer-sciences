# Copyright © 2022 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
# Free under certain conditions — see the license for details.


def main():
    x = list()
    x.append(23)
    x.append(10)
    x.append('Giovanni')
    foo(x)
    # the object bound to 'x' has changed
    print(x)


def foo(y):
    # the object bound to 'y' does change
    y.append(18)
    y.append(5)
    y.append('Paola')


if __name__ == '__main__':
    main()
