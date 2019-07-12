from os import system as sy
from time import sleep


menu = """
0 - sair
1 - programa 1
2 - programa 2
3 - programa 3
4 - programa 4
"""


def main():
    linhas = int(input('digite a quantidade de linhas: '))
    dicio = {'1': range(2, linhas, 2), '2': range(1, linhas),
             '3': range(2, linhas), '4': range(linhas, 0, -1)}
    while True:
        sy('clear')
        print(menu)
        opção = input('opção: ')
        if opção == '0':
            exit()
        elif opção not in '01234':
            raise ValueError('escolha uma opção válida')
        caracter = input('digite o caracter: ')
        for a in dicio[opção]:
            print(caracter * a)
        sleep(1)


if __name__ == '__main__':
    main()
