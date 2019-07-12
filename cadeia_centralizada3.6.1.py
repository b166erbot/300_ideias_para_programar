from os import system as sy, get_terminal_size as get


def main():
    colunas, linhas = get()
    linha = int(input('linha: '))
    if not 0 <= linha <= linhas:
        raise ValueError('erro: linha fora do intervalo permitido')
    caracteres = input('caracteres: ')
    sy('clear')
    print('\n' * (linha - 1))
    print(caracteres.center(colunas))


if __name__ == '__main__':
    main()
