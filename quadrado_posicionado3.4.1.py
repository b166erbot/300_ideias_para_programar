from os import get_terminal_size as get, system as sy


quadrado = """
#####
#   #
#   #
#   #
#####
""".strip().split('\n')


def main():
    linha = int(input('linha: '))
    coluna = int(input('coluna: '))
    b, a = get()
    intervalos = (0 <= linha <= a - 5, 0 <= coluna <= b - 5)
    if not all(intervalos):
        raise ValueError('linha e/ou coluna fora do intervalo permitido')
    sy('clear')
    print('\n' * linha)
    print('\n'.join(f"{' ' * coluna}{a}" for a in quadrado))


if __name__ == '__main__':
    main()
