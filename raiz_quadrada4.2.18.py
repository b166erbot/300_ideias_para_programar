from os import system as sy


menu = """
1 - fim
2 - calcular raiz
""".strip()


def main():
    while True:
        sy('clear')
        print(menu)
        opção = int(input('opção: '))
        if opção == 1:
            break
        elif opção == 2:
            número = float(input('digite um número: '))
            if número >= 0:
                print(f"{número * 0.5:0.2f}")
            else:
                raise ValueError(
                    'não é possível calcular a raiz quadrada de um número negativo')
        else:
            raise ValueError('opção inválida')


if __name__ == '__main__':
    main()
