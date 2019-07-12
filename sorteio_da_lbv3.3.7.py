from re import compile


def main():
    formato = compile(r'^\d{2}\.\d{3}$')
    entrada = input('digite dois prémios: ')
    if not formato.findall(entrada):
        raise ValueError('formato inválido')
    entrada = [a.split('.')[1] for a in entrada.split()]
    print(entrada[0] + '.' + entrada[1])


if __name__ == '__main__':
    main()
