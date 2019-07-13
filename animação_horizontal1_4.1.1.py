from time import sleep
from os import system as sy


def main():
    linha = int(input('digite uma linha: '))
    coluna = int(input('digite uma coluna: '))
    sy('clear')
    for a in range(linha):
        print('\n' * a + 'O', end='\r')
        sleep(0.08)
        sy('clear')
    for b in range(1, coluna + 1):
        print('\n' * a +' ' * b + 'O', end='\r')
        sleep(0.08)
        sy('clear')


if __name__ == '__main__':
    main()
