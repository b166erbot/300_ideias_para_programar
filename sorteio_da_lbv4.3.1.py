from re import compile


def main():
    formato = compile(r'^\d{2}\.\d{3}$')
    entrada = input('digite dois prémios: ')
    while not all(formato.findall(a) for a in entrada.split()):
        print('entrada inválida')
        entrada = input('digite dois prémios: ')
    entrada = [a.split('.')[1] for a in entrada.split()]
    print(entrada[0] + '.' + entrada[1])


if __name__ == '__main__':
    main()
