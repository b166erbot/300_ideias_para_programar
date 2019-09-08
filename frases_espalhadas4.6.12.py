from os import get_terminal_size as get


def main():
    coluna = get()[0]
    if coluna % 2 == 0:
        coluna -= 1
    entradas = []
    entrada = input('digite uma frase: ')
    while entrada:
        string = f"{entrada} {entrada[::-1]}"
        entradas.append(string.center(coluna))
        entrada = input('digite uma frase: ')
    print(*entradas)


if __name__ == '__main__':
    main()
