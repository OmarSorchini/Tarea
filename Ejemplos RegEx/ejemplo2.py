import re


FILE_NAME = 'entrada.txt'


def main():
    with open(FILE_NAME) as archivo:
        info = archivo.read()

    palabras = re.split(r'\n', info)
    print(palabras)


if __name__ == '__main__':
    main()
