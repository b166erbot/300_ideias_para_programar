from random import randint


def main():
    máquina = randint(1, 10)
    while True:
        número = int(input('tente adivinhar o número: '))
        if número == máquina:
            print('acertou!')
            break
        else:
            print('menor' if número > máquina else 'maior')


if __name__ == '__main__':
    main()
