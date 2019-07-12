from functools import reduce
from operator import mul
from math import sqrt


def main():
    entradas = (float(a) for a in input('entradas: ').split())
    media = sqrt(reduce(mul, entradas))
    print(f'{media:0.2f}')


if __name__ == '__main__':
    main()
