def main():
    porcentagem = {6: 'sena', 5: 'quina', 4: 'quadra'}
    apostas = (int(a) for a in input('números da aposta: ').split())
    sorteados = [int(a) for a in input('números sorteados: ').split()]
    acertos = len(tuple(map(lambda x: x in sorteados, apostas)))
    print(porcentagem.get(acertos, 'não acertou o suficiente'))


if __name__ == '__main__':
    main()
