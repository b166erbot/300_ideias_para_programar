from os import get_terminal_size as get, system as sy


quadrado = """
#####
#   #
#   #
#   #
#####
""".strip().split('\n')
triângulo = """
     /\\
    /  \\
   /    \\
  /      \\
 /        \\
/          \\
------------
""".strip('\n').split('\n')


def main():
    opção = int(input('triângulo, quadrado, sair [1/2/3]?: '))
    if opção == 3:
        return print('tchau!')
    linha = int(input('linha: '))
    coluna = int(input('coluna: '))
    b, a = get()
    intervalos = (0 <= linha <= a - 7, 0 <= coluna <= b - 12)
    if not all(intervalos):
        raise ValueError('linha e/ou coluna fora do intervalo permitido')
    sy('clear')
    print('\n' * linha)
    objeto = triângulo if opção == 1 else quadrado
    print('\n'.join(f"{' ' * coluna}{a}" for a in objeto))


if __name__ == '__main__':
    main()
