FILE_NAME = 'entrada.txt'


def main():
    with open(FILE_NAME) as archivo:
        info = archivo.read()

    palabras = info.split()
    print(palabras)


if __name__ == '__main__':
    main()
