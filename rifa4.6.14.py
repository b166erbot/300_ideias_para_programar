def entrada_():
    try:
        return float(input('digite um prêmio: '))
    except:
        pass


def main():
    entradas = []
    entrada = entrada_()
    while entrada:
        if entrada:
            entradas.append(entrada)
        entrada = entrada_()
    print(*(f'{a}-{b:0.3f}' for a, b in enumerate(entradas, 1)), sep='\n')


if __name__ == '__main__':
    main()
