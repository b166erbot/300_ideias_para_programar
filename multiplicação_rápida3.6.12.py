def main():
    valor = input('digite um número entre 10/99: ')
    if 10 > int(valor) or 99 < int(valor):
        raise ValueError('valor fora do intervalo permitido')
    a, b = map(lambda x: int(x), valor)
    c = str(sum((a, b)))
    if len(c) == 2:
        a += int(c[0])
    print(f"{a}{c[-1]}{b}")


if __name__ == '__main__':
    main()
