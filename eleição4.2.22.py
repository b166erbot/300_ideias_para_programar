from os import system as sy
from collections import Counter
from itertools import cycle

menu = """
0 - branco
1 - candidato 1
2 - candidato 2
3 - candidato 3
4 - nulo
5 - votações encerradas
""".strip()


def main():
    O = cycle((0,))
    candidatos = Counter(dict([a, next(O)] for a in range(5)))
    while True:
        sy('clear')
        print(menu)
        opção = int(input('opção: '))
        if opção == 5:
            break
        candidatos[opção] += 1
    import pdb; pdb.set_trace()
    sy('clear')
    items = list(candidatos.items())[1:-1]
    print('vencedor:', max(items, key=lambda x: x[1])[0])
    print('votos brancos:', candidatos[4])
    print('votos nulos:', candidatos[0])
    print('número de eleitores que votaram:', sum(candidatos.values()))


if __name__ == '__main__':
    main()
