from functools import reduce


def main():
    números = [int(a) for a in input('digite 3 números de 32 - 254: ').split()]
    if any((a not in range(32, 255) for a in números)):
        raise ValueError('algum(ns) número(s) está(ão) fora do intervalo.')
    print(reduce(lambda x, y: x + y, (chr(a) for a in números)))


if __name__ == '__main__':
    main()
