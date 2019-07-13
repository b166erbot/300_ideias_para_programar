from os import system as sy


menu = """
1 - adicionar notas
2 - pesquisar nota
3 - visualizar notas
4 - sair
"""


def main():
    notas = []
    while True:
        sy('clear')
        print(menu)
        opção = int(input('opção: '))
        if opção == 1:
            for a in range(1, 11):
                nota = float(input(f"nota {a}: "))
                while nota not in range(0, 11):
                    nota = float(input(f"nota {a}: "))
                notas.append(nota)
        elif opção == 2:
            nota = float(input('nota à ser pesquisada: '))
            while nota not in range(0, 11):
                nota = float(input('nota à ser pesquisada: '))
            print('nota no vetor' if nota in notas else 'nota fora do vetor')
            input('precione enter para continuar')
        elif opção == 3:
            print(*notas)
            input('precione enter para continuar')
        else:
            break


if __name__ == '__main__':
    main()
