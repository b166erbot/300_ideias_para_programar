from os import system as sy
from time import sleep


def entrada():
    dicio = {2: 'cadastro',3: 'consulta'}
    try:
        opção = int(input('opção: '))
        if opção in range(1, 4):
            if opção == 1:
                exit()
            else:
                print(f"você escolheu a opção {dicio[opção]}")
                sleep(1)
        else:
            print('opção inválida')
            sleep(1)
    except ValueError:
        print('opção inválida')


menu = """
1 - Fim
2 - Cadastro
3 - Consulta
""".strip()


def main():
    while True:
        sy('clear')
        print(menu)
        entrada()


if __name__ == '__main__':
    main()
