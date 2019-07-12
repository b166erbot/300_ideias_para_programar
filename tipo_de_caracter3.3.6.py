from re import compile


def main():
    aritiméticos = compile(r'[\+\-/%\*]{1,2}')
    entrada = input('digite um caracter: ')
    if entrada.isdigit():
        print('o caracter é um digito')
    elif entrada.isalpha():
        print('o caracter é uma letra')
    elif aritiméticos.findall(entrada):
        print('o caracter é um operador aritimético')
    else:
        print('o caracter não é uma letra, digito ou operador aritimético')


if __name__ == '__main__':
    main()
