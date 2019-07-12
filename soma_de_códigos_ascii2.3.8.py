from functools import reduce


def main():
    entrada = input('digite 3 caracteres: ')
    print(reduce(lambda x, y: x + y, [ord(a) for a in entrada]))


if __name__ == '__main__':
    main()
