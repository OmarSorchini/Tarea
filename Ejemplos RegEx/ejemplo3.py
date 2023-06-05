import re


FILE_NAME = 'entrada.txt'


def main():
    with open(FILE_NAME) as archivo:
        info = archivo.read()

    for m in re.finditer(r"(\w|')+", info):
        print(m[0].upper())


if __name__ == '__main__':
    main()
