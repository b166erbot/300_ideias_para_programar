def main():
    notas_pesos = []
    notaPeso = [float(a) for a in input('digite uma nota e um peso: ').split()]
    while notaPeso[0] > 0:
        notas_pesos.append(notaPeso)
        entrada = input('digite uma nota e um peso: ')
        notaPeso = [float(a) for a in entrada.split()]
    resultado = sum(map(lambda x: x[0] * x[1], notas_pesos)) / len(notas_pesos)
    print(f"{resultado:0.1f}")



if __name__ == '__main__':
    main()
