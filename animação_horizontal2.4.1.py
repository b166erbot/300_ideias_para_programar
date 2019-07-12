from os import get_terminal_size as get, system as sy


def main():
    entrada = int(input('digite o número da coluna: '))
    for a in range(10):
        sy('clear')
        print(' ' * get()[0] + '\n' * a)
        print(f"\r{' ' * entrada}O")
        input('pressione enter para continuar.')


if __name__ == '__main__':
    main()
