# Copyright © 2021 Giovanni Squillero <giovanni.squillero@polito.it>
# https://github.com/squillero/computer-sciences
# Free under certain conditions — see the license for details.


def get_file_list():
    text = input('List of files: ')
    files = list()
    for file in text.split(','):
        files.append(file.strip())
    return files


def search(filename, text):
    try:
        with open(filename) as input_:
            for line in input_:
                if text.casefold() in line.casefold():
                    print(f"{filename}: {line[:-1]}")
    except OSError as error:
        print(f"ERROR: {error}")


def main():
    files = get_file_list()
    text = input('Text: ')
    for file in files:
        search(file, text)


if __name__ == '__main__':
    main()
