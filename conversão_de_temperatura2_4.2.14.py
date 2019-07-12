from os import get_terminal_size as get


def main():
    colunas = get()[0]
    inicial = int(input('inicial: '))
    final = int(input('final: '))
    variação = int(input('variação: '))
    print('Tabela de temperaturas.'.center(colunas))
    print('-' * colunas)
    for celsius in range(inicial, final, variação):
        fahrenheit = celsius * 9 / 5 + 32
        print(f"celcius:  {celsius} | fahrenheit:   {fahrenheit}")
        input('aperte enter.')


if __name__ == '__main__':
    main()
