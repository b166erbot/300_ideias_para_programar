def main():
    valor = float(input('digite um valor: ').replace(',', '.'))
    if valor >= 0:
        print(valor ** 0.5)
    else:
        raise ValueError('valor menor que zero não é possível calcular aqui.')


if __name__ == '__main__':
    main()
