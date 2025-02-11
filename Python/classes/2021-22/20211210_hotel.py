# Copyright © 2021 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
# Free under certain conditions — see the license for details.

from pprint import pprint

DATAFILE = '20211210_hotel.dat'


def main():
    total = dict()
    with open(DATAFILE) as data:
        for line in data:
            customer_r, service_r, price_r, date_r = line.split(';')
            customer = customer_r.strip()
            service = service_r.strip().casefold()
            price = float(price_r)
            date = date_r.strip()

            if service not in total:
                total[service] = price
            else:
                total[service] += price

        for key in sorted(total):
            print(f"{key} -> {total[key]}")


if __name__ == '__main__':
    main()
