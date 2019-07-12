from functools import reduce


def main():
    entrada = input('digite seu nome completo: ').split()
    print(reduce(lambda x, y: x + y, (a[-1] for a in entrada)))


if __name__ == '__main__':
    main()
