def main():
    valor = float(input('digite o valor da aposta R$: ').replace(',', '.'))
    if valor > 100:
        raise ValueError('valor inserido excede o limite permitido de R$100')
    fichas = {'branca branca': 0, 'branca preta': 0.5, 'preta branca': 1,
              'preta preta': 2}
    sorteadas = input('digite as duas fichas: ').lower()
    resultado = fichas[sorteadas] * valor
    resultado = int(resultado) if int(resultado) == resultado else resultado
    print(resultado)


if __name__ == '__main__':
    main()
