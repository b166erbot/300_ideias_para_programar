quadrado = """
#####
#   #
#   #
#   #
#####
""".strip().split('\n')


def main():
    linha = int(input('linha: '))
    coluna = int(input('coluna: '))
    print('\n' * linha)
    temp = '\n'.join([' ' * coluna + a for a in quadrado])
    print(temp)


if __name__ == '__main__':
    main()
