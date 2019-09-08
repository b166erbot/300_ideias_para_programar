def main():
    notas = (100, 50, 20, 10, 5, 2)
    moedas = (1, 0.50, 0.25, 0.10, 0.5, 0.01)
    entrada = float(input('R$: '))
    q_notas = []
    q_moedas = []
    forma = '{} {} de {}'
    for nota in notas:
        if entrada % nota != entrada:
            # import pdb; pdb.set_trace()
            resto = entrada % nota
            q_notas.append(((entrada - resto) // nota, nota))
            entrada = resto
    for moeda in moedas:
        if entrada % moeda != entrada:
            # import pdb; pdb.set_trace()
            resto = entrada % moeda
            q_moedas.append(((entrada - resto) // moeda, moeda))
            entrada = resto
    for quantidade, nota in q_notas:
        print(forma.format(quantidade, 'notas', nota))
    for quantidade, moeda in q_moedas:
        print(forma.format(quantidade, 'moedas', moeda))


if __name__ == '__main__':
    main()
