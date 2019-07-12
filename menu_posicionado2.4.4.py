from os import system as sy, get_terminal_size as get


def main():
    menu = """
    Menu de consultas
    0 - Fim
    1 - Clientes
    2 - Produtos
    3 - Faturas
    4 - Estoque
    """.strip().split('\n')
    coluna = int(input('digite a coluna: '))
    menu = '\n'.join((' ' * coluna + a for a in menu))
    while True:
        sy('clear')
        print(menu)
        opção = input('opção: ')
        if not opção:
            exit()


if __name__ == '__main__':
    main()
