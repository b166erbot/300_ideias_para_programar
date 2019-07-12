from os import get_terminal_size as get


def main():
    linha = int(input('linha: '))
    coluna = int(input('coluna: '))
    iniciais = input('Iniciais: ')
    print('\n' * linha)
    for a in range(1, 8, 2):
        if a != 7:
            print(' ' * coluna + f"/{' ' * a}\\".center(11))
        else:
            print(' ' * coluna + f"/{iniciais.center(7)}\\".center(11))
    print(' ' * coluna + ('-' * (a + 2)).center(11))
    input('digite ENTER para sair.')


if __name__ == '__main__':
    main()
