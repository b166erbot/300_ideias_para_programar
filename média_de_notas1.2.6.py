def moldura(valor: str):
    print('-' * (len(valor) + 4))
    print(f'| {valor} |')
    print('-' * (len(valor) + 4))


def main():
    notas = [float(a) for a in input('notas: ').split()]
    média = sum(notas) / len(notas)
    moldura(f'{média:0.2f}')


if __name__ == '__main__':
    main()
