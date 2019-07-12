from os import system as sy
from time import sleep


def main():
    a, b, c, d, e, f = '═║╔╗╚╝'
    funcoes = {'1': nome, '2': codigo, '3': data}
    while True:
        sy('clear')
        print(c + a * 78 + d)
        print(b + ' ' * 78 + b)
        print(b + ' ' * 10 + 'Menu Relatórios' + ' ' * 53 + b)
        print(b + ' ' * 78 + b)
        print(b + ' ' * 10 + '1 - Por nome' + ' ' * 56 + b)
        print(b + ' ' * 10 + '2 - Por código' + ' ' * 54 + b)
        print(b + ' ' * 10 + '3 - Por data' + ' ' * 56 + b)
        print(b + ' ' * 10 + '4 - Fim' + ' ' * 61 + b)
        print(b + ' ' * 78 + b)
        print(e + a * 78 + f)
        funcoes.get(input('Opção: '), exit)()
        sleep(1)


def nome():
    print('\n\naqui devem ser impressos os relatórios por nome')


def codigo():
    print('\n\naqui devem ser impressos os relatórios por código')


def data():
    print('\n\naqui devem ser impressos os relatórios por data')


if __name__ == '__main__':
    main()
