from os import get_terminal_size as get


def main():
    letra = input('Letra: ')
    iniciais = input('Iniciais: ')
    for a in range(1, 8, 2):
        if a != 7:
            print(f'{letra}{" " * a}{letra}'.center(11))
        else:
            print(f"{letra}{iniciais.center(7)}{letra}".center(11))
    print((letra * (a + 2)).center(11))
    input('digite ENTER para sair.')


if __name__ == '__main__':
    main()
