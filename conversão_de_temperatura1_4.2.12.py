from os import get_terminal_size as get


def main():
    colunas = get()[0]
    print('Tabela de temperaturas.'.center(colunas))
    print('-' * colunas)
    for celsius in range(1, 101):
        fahrenheit = celsius * 9 / 5 + 32
        print(f"celcius:  {celsius} | fahrenheit:   {fahrenheit}")
        input('aperte enter.')


if __name__ == '__main__':
    main()
