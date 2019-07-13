from os import system as sy


menu = """
1 - saque
2 - depósito
3 - quantidade de notas / valor total de saque
4 - exit
"""


def main():
    notas = ([10, 500], [50, 100])
    total_saque = 0
    while True:
        sy('clear')
        print(menu)
        opção = int(input('opção: '))
        if opção == 1:
            saque = float(input('digite o valor a sacar: '))
            resto50 = saque % 50
            quantidade = (saque - resto50) // 50
            if quantidade > notas[1][1]:
                raise SystemError('não há notas de 50 o suficiente')
            resto10 = resto50 % 10
            if resto10 > 0:
                raise ValueError('suas notas precisam ser mod de 50 e/ou 10')
            quantidade2 = resto50 // 10
            if quantidade2 > notas[0][1]:
                raise SystemError('não há notas de 10 o suficiente')
            notas[1][1] -= quantidade
            notas[0][1] -= quantidade2
            total_saque += saque
            print(f"saque de {saque} com {50 * quantidade} notas de 50\n"
                  f"e {10 * quantidade2} notas de 10")

        elif opção == 2:
            depósito = float(input('digite o valor para o depósito:'))
            resto50 = depósito % 50
            quantidade = (depósito - resto50) // 50
            resto10 = resto50 % 10
            if resto10 > 0:
                raise SystemError('suas notas precisam ser mod de 50 e/ou 10')
            quantidade2 = resto50 // 10
            notas[1][1] += quantidade
            notas[0][1] += quantidade2
            print(f"depósito de {depósito} com {50 * quantidade} notas de 50\n"
                  f"e {10 * quantidade2} notas de 10")
        elif opção == 3:
            print(f"notas de 50 = {notas[1][1]}, notas de 10 = {notas[0][1]}")
            print(f"valor total de saque = {total_saque}")
        else:
            exit()
        input('precione enter para continuar')


if __name__ == '__main__':
    main()
